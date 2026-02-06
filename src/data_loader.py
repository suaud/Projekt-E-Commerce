import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import time
import random
import re

class DataLoader:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/115.0.0.0 Safari/537.36",
            "Accept-Language": "pl-PL"
        }
        
        elektronika = ['iPhone 13', 'Samsung Galaxy S23', 'Xiaomi Redmi', 'PlayStation 5', 'Xbox Series X', 'Laptop Dell', 'Karta graficzna', 'Monitor 144Hz', 'Sluchawki Sony', 'Myszka Logitech']
        gry = ['Wiedźmin 3', 'Cyberpunk 2077', 'GTA V', 'FIFA 24', 'Call of Duty', 'God of War', 'Spider-Man 2', 'Mario Bros', 'The Sims 4', 'Baldurs Gate 3']
        ksiazki = ['Harry Potter', 'Władca Pierścieni', 'Hobbit', 'Lalka', 'Pan Tadeusz', 'Krzyżacy', 'Metro 2033', 'Diuna', 'Opowieści z Narnii']
        zabawki = ['Lego Star Wars', 'Barbie', 'Monopoly', 'Puzzle 1000', 'Hot Wheels', 'Pluszak', 'Klocki COBI']
        ubrania = ['Nike Air Max', 'Adidas Ultraboost', 'Kurtka zimowa', 'Jeansy Levis', 'Bluza z kapturem', 'T-shirt bawelniany']
        inne = ['test', 'błąd', 'asdf', 'sprawdzam', 'latajacy toster', 'nic', 'szukam']

        self.train_df = pd.DataFrame({
            'text': (elektronika + gry + ksiazki + zabawki + ubrania + inne) * 15, 
            'category': (
                ['Elektronika']*len(elektronika) + 
                ['Gry']*len(gry) + 
                ['Ksiazki']*len(ksiazki) + 
                ['Zabawki']*len(zabawki) + 
                ['Ubrania']*len(ubrania) +
                ['Inne']*len(inne)
            ) * 15
        })

    def get_training_data(self):
        return self.train_df

    def scrape_ceneo(self, query):
        url = f"https://www.ceneo.pl/;szukaj-{urllib.parse.quote(query)}"
        data = []

        try:
            time.sleep(random.uniform(0.3, 0.6))
            r = requests.get(url, headers=self.headers, timeout=5)
            if r.status_code != 200: return []

            soup = BeautifulSoup(r.text, 'html.parser')
            products = soup.select("div.cat-prod-row") or soup.select("div.grid-row")
            
            if not products: return []

            forbidden = [
                "etui", "case", "szkło", "folia", "uchwyt", "bateria", "pasek", "ładowarka", 
                "kalendarz", "figurka", "puzzle", "plakat", "kubek", "koszulka", "brelok",
                "poradnik", "soundtrack", "muzyka", "dlc", "dodatek", "klucz", "cyfrowa",
                "portal", "remote", "pilot"
            ]

            q_tokens = [w for w in query.lower().split() if len(w) > 0]

            for prod in products[:25]:
                try:
                    name_tag = prod.select_one("strong.cat-prod-row__name, span.grid-item__name")
                    if not name_tag: continue
                    
                    name = name_tag.text.strip()
                    name_lower = name.lower()
                    prod_words = set(re.findall(r'\w+', name_lower))

                    match = True
                    for token in q_tokens:
                        if token.isdigit():
                            if token in prod_words: continue
                            
                            is_unit = False
                            for u in ['gb', 'tb', 'mb', 'kg', 'ml']:
                                if (token + u) in name_lower:
                                    is_unit = True
                                    break
                            
                            if is_unit: continue
                            match = False
                            break
                        else:
                            if token not in name_lower:
                                match = False
                                break
                    
                    if not match: continue

                    if any(f in name_lower and f not in query.lower() for f in forbidden):
                        continue

                    price_int = prod.select_one("span.value").text.strip()
                    price_penny = prod.select_one("span.penny").text.strip()
                    price = float(f"{price_int}{price_penny}".replace(" ", "").replace(",", "."))

                    data.append({'product_name': name, 'price': price})
                except:
                    continue

            return data

        except Exception:
            return []

    def get_live_data(self, query):
        res = self.scrape_ceneo(query)
        return pd.DataFrame(res) if res else pd.DataFrame()
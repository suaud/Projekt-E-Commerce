import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.getcwd())

from src.data_loader import DataLoader
from src.preprocessor import DataPreprocessor
from src.model import ProductClassifier

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_stats(df):
    prices = df['price']
    print(f"\n{Colors.YELLOW}Statystyki:{Colors.RESET}")
    print(f"Średnia:    {np.mean(prices):.2f} zł")
    print(f"Mediana:    {np.median(prices):.2f} zł")
    print(f"Odchylenie: {np.std(prices):.2f} zł")
    
    try:
        counts, bins = np.histogram(prices, bins=5)
        print("\nRozkład cen:")
        for i in range(len(counts)):
            bar = '█' * int(counts[i])
            print(f"{bins[i]:.0f}-{bins[i+1]:.0f} | {bar} ({counts[i]})")
    except:
        pass

def main():
    print(f"{Colors.BOLD}=== E-Commerce Price Analyzer (CENEO) ==={Colors.RESET}")
    
    loader = DataLoader()
    proc = DataPreprocessor()
    model = ProductClassifier()

    train_data = loader.get_training_data()
    model.train(train_data['text'], train_data['category'])

    while True:
        try:
            q = input(f"\n{Colors.HEADER}Szukaj {Colors.RESET}(lub '{Colors.RED}exit{Colors.RESET}'): ").strip()
            if q == 'exit': break
            if len(q) < 2: continue

            cat = model.predict(q)
            print(f"Kategoria: {Colors.BLUE}{cat}{Colors.RESET}")

            df = loader.get_live_data(q)
            if df.empty:
                print(f"{Colors.RED}Brak wyników.{Colors.RESET}")
                continue

            df['clean'] = df['product_name'].apply(proc.clean_text)
            df = df.sort_values('price')
            
            if len(df) > 5:
                df = df[df['price'] < df['price'].iloc[0] * 5]

            print_stats(df)
            
            avg_price = df['price'].mean()

            print("-" * 50)
            print(f"{'PRODUKT':<50} | {'CENA':<12}")
            print("-" * 50)
            
            for i, row in df.head(15).iterrows():
                price = row['price']
                name = row['product_name'][:48]
                
                if i == df.index[0]:
                    p_str = f"{Colors.GREEN}{price:>8.2f} zł ⭐{Colors.RESET}"
                elif price > avg_price:
                    p_str = f"{Colors.RED}{price:>8.2f} zł{Colors.RESET}"
                else:
                    p_str = f"{price:>8.2f} zł"

                print(f"{name:<50} | {p_str}")
            print("-" * 50)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
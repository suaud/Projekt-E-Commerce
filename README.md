# Projekt zaliczeniowy: E-Commerce Price Analyzer (CENEO)

**Autorzy:** Oliwier Gołosko, Szymon Cieszyński, Kacper Brant  
**Przedmiot:** Uczenie maszynowe w Pythonie  
**Rok akademicki:** 2025/2026

---

## 1. Opis projektu

**E-Commerce Price Analyzer** to aplikacja konsolowa (CLI) przeznaczona do analizy cen produktów dostępnych na platformie **Ceneo.pl**. Projekt wykorzystuje elementy **uczenia maszynowego**, w szczególności model *Naive Bayes*, do automatycznego rozpoznawania kategorii produktu na podstawie wprowadzonej przez użytkownika nazwy.

Program pobiera aktualne oferty w czasie rzeczywistym, filtruje niepożądane wyniki (np. akcesoria lub cyfrowe klucze), a następnie prezentuje szczegółową analizę cen. Użytkownik otrzymuje m.in. średnią cenę, medianę, odchylenie standardowe oraz histogram rozkładu cen, a także prostą rekomendację zakupu.

---

## 2. Kluczowe funkcjonalności

- **Scraping danych**  
  Pobieranie nazw oraz cen produktów z serwisu Ceneo.pl z wykorzystaniem bibliotek `requests` i `BeautifulSoup`.

- **Klasyfikacja oparta na ML**  
  Model uczenia maszynowego zbudowany przy użyciu `scikit-learn`, trenowany na danych tekstowych z zastosowaniem wektorów TF-IDF, automatycznie określa kategorię produktu.

- **Analiza statystyczna cen**  
  Obliczanie podstawowych miar statystycznych: średniej, mediany oraz odchylenia standardowego.

- **Inteligentne filtrowanie wyników**  
  - rozróżnianie jednostek i pojemności (np. „256 GB” vs „256”),  
  - wykorzystanie czarnej listy produktów (np. etui, szkła ochronne, pady przy wyszukiwaniu konsol).

- **Interfejs konsolowy (CLI)**  
  - kolorowe oznaczenia cen (🟢 tanio / 🔴 drogo),  
  - histogram rozkładu cen w formie ASCII,  
  - raport jakości klasyfikacji (precision, recall).

---

## 3. Instalacja i uruchomienie

### Krok 1: Instalacja Pythona (wersja 3.8 lub nowsza)

**Windows**  
Pobierz instalator ze strony [python.org](https://www.python.org/downloads/).  
Podczas instalacji upewnij się, że zaznaczona jest opcja **Add Python to PATH**.

**Linux (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

**macOS**
```bash
brew install python
```

---

### Krok 2: Instalacja zależności

W katalogu projektu uruchom terminal i wykonaj polecenie:

```bash
# Windows
pip install -r requirements.txt

# Linux / macOS
pip3 install -r requirements.txt
```

W przypadku problemów z uprawnieniami należy poprzedzić komendę słowem `sudo`.

---

### Krok 3: Uruchomienie aplikacji

```bash
# Windows
python main.py

# Linux / macOS
python3 main.py
```

---

## 4. Instrukcja użytkowania

1. **Uruchomienie programu**  
   Po starcie aplikacji należy poczekać na załadowanie oraz trenowanie modelu uczenia maszynowego. Postęp widoczny jest w konsoli.

2. **Wyszukiwanie produktu**  
   Wprowadź nazwę produktu, np. `iPhone 13` lub `PlayStation 5`.

3. **Prezentacja wyników**  
   Program wyświetli:
   - przewidywaną kategorię produktu,  
   - statystyki cenowe (średnia, mediana, odchylenie standardowe),  
   - histogram rozkładu cen,  
   - listę znalezionych ofert, gdzie najtańsza oznaczona jest symbolem ⭐.

4. **Kolejne wyszukiwanie**  
   Naciśnij klawisz Enter, aby wyczyścić ekran i rozpocząć nowe wyszukiwanie.

5. **Zakończenie pracy**  
   Wpisz `exit`, aby zamknąć aplikację.

---

## 5. Wykorzystywane biblioteki

- `requests`  
- `beautifulsoup4`  
- `pandas`  
- `scikit-learn`  
- `numpy`


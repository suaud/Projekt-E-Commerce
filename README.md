# Projekt Zaliczeniowy: E-Commerce Price Analyzer

**Autor:** Oliwier Gołosko, Szymon Cieszyński, Kacper Brant
**Przedmiot:** Uczenie maszynowe w Python

## 1. Opis Problemu
Celem projektu jest stworzenie narzędzia do pobierania i analizy cen produktów z serwisu Ceneo.pl w czasie rzeczywistym. System wykorzystuje techniki Scrapingu do pozyskania danych oraz Machine Learning do automatycznej kategoryzacji zapytań użytkownika.

## 2. Zrealizowane Wymagania
1. **Pobieranie danych:** Crawler oparty na `requests` i `BeautifulSoup` pobiera oferty z Ceneo.
2. **Przetwarzanie danych:** Zaimplementowano rygorystyczne filtry usuwające akcesoria (etui, szkła) oraz niezgodne modele. Normalizacja tekstu w klasie `DataPreprocessor`.
3. **OOP:** Kod podzielony na klasy: `DataLoader`, `DataPreprocessor`, `ProductClassifier`.
4. **Machine Learning:** Model `Naive Bayes` trenowany na danych tekstowych (TF-IDF) przewiduje kategorię produktu (np. Electronics, Books).
5. **Analiza:** Program oblicza średnią cenę rynkową oraz wskazuje najtańszą ofertę.

## 3. Instrukcja Uruchomienia
1. Zainstaluj biblioteki: `pip install -r requirements.txt`
2. Uruchom program: `python main.py`
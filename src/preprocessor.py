import re

class DataPreprocessor:
    def clean_text(self, text):
        if not isinstance(text, str): return ""
        text = text.lower()
        text = re.sub(r'[^a-z0-9\sąćęłńóśźż]', '', text)
        return re.sub(r'\s+', ' ', text).strip()
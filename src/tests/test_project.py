import unittest
import sys
import os
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessor import DataPreprocessor
from src.model import ProductClassifier

class TestEcommerceProject(unittest.TestCase):
    
    def setUp(self):

        self.processor = DataPreprocessor()
        self.classifier = ProductClassifier()

    def test_normalization(self):

        raw_text = "iPhone 13 Pro!!! @#$"
        expected = "iphone 13 pro"
        result = self.processor.clean_text(raw_text)
        self.assertEqual(result, expected)

    def test_normalization_polish_chars(self):

        raw_text = "Mąka pszenna"
        expected = "mąka pszenna"
        result = self.processor.clean_text(raw_text)
        self.assertEqual(result, expected)

    def test_model_training_and_prediction(self):

        df = pd.DataFrame({
            'text': ['iphone', 'samsung', 'harry potter', 'wiedźmin'],
            'category': ['Electronics', 'Electronics', 'Books', 'Books']
        })
        
        # Trening
        self.classifier.train(df['text'], df['category'])
        

        prediction = self.classifier.predict("iphone")
        self.assertEqual(prediction, "Electronics")
        
        prediction_book = self.classifier.predict("harry")
        self.assertEqual(prediction_book, "Books")

if __name__ == '__main__':
    unittest.main()
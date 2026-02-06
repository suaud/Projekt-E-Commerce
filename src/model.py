from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix

class ProductClassifier:
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB())
        ])
        
        self.params = {
            'tfidf__ngram_range': [(1, 1), (1, 2)],
            'clf': [MultinomialNB(), SGDClassifier(loss='hinge', random_state=42)]
        }
        
        self.gs = GridSearchCV(self.pipeline, self.params, cv=5, n_jobs=1)

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        
        self.gs.fit(X_train, y_train)
        
        print(f"Accuracy: {self.gs.best_score_:.2f}")
        print(f"Model: {self.gs.best_estimator_.named_steps['clf']}")

        y_pred = self.gs.predict(X_test)
        
        report = classification_report(y_test, y_pred)
        
        replacements = {
            "precision": "precyzja",
            "recall": "czułość ",
            "f1-score": "f1-wynik",
            "support": "ilość   ",
            "accuracy": "dokładność",
            "macro avg": "śr. macro ",
            "weighted avg": "śr. ważona"
        }
        
        for en, pl in replacements.items():
            report = report.replace(en, pl)

        print("\n--- RAPORT ---")
        print(report)
        print(confusion_matrix(y_test, y_pred))
        print("-" * 20)

    def predict(self, text):
        return self.gs.predict([text])[0]
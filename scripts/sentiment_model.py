# scripts/sentiment_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROC = BASE / "data" / "processed"
MODELS = BASE / "models"
MODELS.mkdir(parents=True, exist_ok=True)

def label_from_rating(r):
    # treat ratings >=7 as positive, <=4 negative, else neutral -- adjust as needed
    if r >= 7: return "positive"
    if r <= 4: return "negative"
    return "neutral"

def train():
    df = pd.read_csv(PROC / "cleaned_reviews.csv")
    df = df.dropna(subset=['clean_review','rating'])
    df['label'] = df['rating'].apply(label_from_rating)
    # For binary sentiment, keep positive vs negative (drop neutral)
    df = df[df['label'] != 'neutral']
    X = df['clean_review']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=20000, ngram_range=(1,2))),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)
    print(classification_report(y_test, preds))
    joblib.dump(pipeline, MODELS / "tfidf_logreg.pkl")
    print("Model saved to", MODELS / "tfidf_logreg.pkl")

if __name__ == "__main__":
    train()

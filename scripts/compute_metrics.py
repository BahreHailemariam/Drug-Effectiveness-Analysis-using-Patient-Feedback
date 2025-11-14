# scripts/compute_metrics.py
import pandas as pd
from pathlib import Path
import joblib
import numpy as np

BASE = Path(__file__).resolve().parents[1]
PROC = BASE / "data" / "processed"
OUT = BASE / "data" / "processed"
MODELS = BASE / "models"

def compute_dei():
    df = pd.read_csv(PROC / "cleaned_reviews.csv")
    model = joblib.load(MODELS / "tfidf_logreg.pkl")
    # predict probabilities for positive class
    probs = model.predict_proba(df['clean_review'])
    # get index of positive class
    classes = model.classes_
    if 'positive' in classes:
        pos_idx = list(classes).index('positive')
        pos_prob = probs[:, pos_idx]
    else:
        pos_prob = np.zeros(len(df))
    # normalize rating to 0-1
    df['rating_norm'] = df['rating'] / 10.0
    df['sentiment_score'] = pos_prob  # between 0-1
    df['DEI'] = 0.6*df['rating_norm'] + 0.4*df['sentiment_score']
    df.to_csv(OUT / "metrics_with_dei.csv", index=False)
    # aggregate by drugName, condition
    agg = df.groupby(['drugName','condition']).agg(
        avg_dei=('DEI','mean'),
        avg_rating=('rating','mean'),
        avg_sentiment=('sentiment_score','mean'),
        review_count=('DEI','count')
    ).reset_index().sort_values('avg_dei', ascending=False)
    agg.to_csv(OUT / "drug_condition_dei.csv", index=False)
    print("Saved metrics and aggregates.")

if __name__ == "__main__":
    compute_dei()

# scripts/clean_text.py
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from pathlib import Path

nltk.download('stopwords', quiet=True)
STOP = set(stopwords.words('english'))

BASE = Path(__file__).resolve().parents[1]
PROC = BASE / "data" / "processed"

def clean_text(s):
    if pd.isna(s): return ""
    s = str(s).lower()
    s = re.sub(r"http\S+","", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    tokens = [t for t in s.split() if t not in STOP and len(t)>2]
    return " ".join(tokens)

def main():
    df = pd.read_csv(PROC / "raw_loaded.csv")
    df['clean_review'] = df['review'].apply(clean_text)
    df.to_csv(PROC / "cleaned_reviews.csv", index=False)
    print("Saved cleaned_reviews.csv")

if __name__ == "__main__":
    main()

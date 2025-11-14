# scripts/load_data.py
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW = DATA_DIR / "raw"
PROCESSED = DATA_DIR / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

def load_csv(fname="reviews.csv"):
    df = pd.read_csv(RAW / fname)
    df.to_csv(PROCESSED / "raw_loaded.csv", index=False)
    print("Loaded:", df.shape)
    return df

if __name__ == "__main__":
    load_csv()

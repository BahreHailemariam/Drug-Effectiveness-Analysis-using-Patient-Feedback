# scripts/visualize_results.py
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "data" / "processed"
agg = pd.read_csv(OUT / "drug_condition_dei.csv")

def top_drugs_plot(n=10):
    top = agg.head(n)
    fig = px.bar(top, x='drugName', y='avg_dei', color='avg_dei', title='Top Drugs by DEI')
    fig.write_html(OUT / "top_drugs_by_dei.html")
    print("Saved HTML plot for top drugs.")

if __name__ == "__main__":
    top_drugs_plot()

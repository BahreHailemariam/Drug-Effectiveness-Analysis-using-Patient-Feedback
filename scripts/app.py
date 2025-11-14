# scripts/app.py
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

BASE = Path(__file__).resolve().parents[1]
PROC = BASE / "data" / "processed"

st.set_page_config(page_title="Drug Effectiveness Explorer", layout="wide")
st.title("Drug Effectiveness Analysis (DEI)")

@st.cache_data
def load_data():
    agg = pd.read_csv(PROC / "drug_condition_dei.csv")
    raw = pd.read_csv(PROC / "metrics_with_dei.csv")
    return agg, raw

agg, raw = load_data()

drug = st.sidebar.selectbox("Select drug", options=agg['drugName'].unique())
condition = st.sidebar.selectbox("Condition", options=agg['condition'].unique())

filtered = raw[(raw['drugName']==drug) & (raw['condition']==condition)]
st.header(f"{drug} — {condition}")
st.metric("Average DEI", f"{filtered['DEI'].mean():.3f}", delta=None)
st.subheader("Review distribution")
fig = px.histogram(filtered, x='DEI', nbins=20)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Recent Reviews (sample)")
st.dataframe(filtered[['date','rating','DEI','review']].head(20))

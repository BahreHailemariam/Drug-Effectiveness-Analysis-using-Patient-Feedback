# 💊 Drug Effectiveness Analysis using Patient Feedback
## 🧠 Overview

This project analyzes **patient feedback and sentiment** to evaluate the effectiveness of drugs prescribed for specific medical conditions.
By combining **Natural Language Processing (NLP), sentiment analysis**, and **statistical modeling**, the pipeline identifies trends in drug performance and patient satisfaction based on real-world reviews.

The goal is to help healthcare providers, pharmaceutical researchers, and regulators **derive data-driven** insights into how different drugs perform in real-world scenarios.
## 🎯 Business Problem

Pharmaceutical companies and health data analysts often rely on clinical trials to evaluate drug performance — but these trials don’t always reflect real-world patient experiences.
This project bridges that gap by analyzing **textual feedback** from patients (e.g., online reviews, surveys) to:

- Identify top-performing drugs based on sentiment and ratings.

- Detect side effects and recurring patient complaints.

- Evaluate overall treatment effectiveness by condition and demographic.

## 🔍 Objectives

- Collect and preprocess patient reviews from public datasets or APIs.

- Perform sentiment classification (positive, neutral, negative).

- Compute drug effectiveness scores using aggregated feedback.

- Visualize sentiment trends and satisfaction levels across conditions.

- Generate Power BI dashboards for business and clinical insights.

## 🧩 Dataset

Example dataset (from [UCI Drug Review Dataset]{https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29}
):
| Feature       | Description                                  |
| ------------- | -------------------------------------------- |
| `drugName`    | Name of the prescribed drug                  |
| `condition`   | Medical condition being treated              |
| `review`      | Text feedback written by the patient         |
| `rating`      | Numerical rating (1–10)                      |
| `date`        | Review submission date                       |
| `usefulCount` | Number of users who found the review helpful |

## ⚙️ Tech Stack

| Layer                        | Tools / Libraries                                            |
| ---------------------------- | ------------------------------------------------------------ |
| **Data Collection**          | `pandas`, `requests`, CSV/JSON APIs                          |
| **Data Cleaning**            | `re`, `nltk`, `textblob`, `scikit-learn`                     |
| **NLP & Sentiment Analysis** | `VADER`, `TextBlob`, or fine-tuned `BERT`                    |
| **Visualization**            | `matplotlib`, `seaborn`, `wordcloud`, `Plotly`, **Power BI** |
| **Automation**               | `schedule`, `Flask`, `Airflow` (optional)                    |
| **Deployment**               | Streamlit / Power BI Dashboards                              |

## 🧮 Project Workflow
### 1️⃣ Data Extraction

- Import CSV reviews dataset or pull live reviews via API.

- Store raw data in `/data/raw/`.

### 2️⃣ Data Cleaning

- Remove stopwords, punctuation, and special characters.

- Normalize case, handle missing values, and remove duplicates.

- Save processed data in `/data/processed/`.

### 3️⃣ Sentiment Analysis

- Apply **VADER** or **TextBlob** sentiment scoring:
```python
from textblob import TextBlob
df['sentiment_score'] = df['review'].apply(lambda x: TextBlob(x).sentiment.polarity)
```
- Classify reviews:
```python
  df['sentiment_label'] = df['sentiment_score'].apply(lambda s: 'Positive' if s>0 else ('Negative' if s<0 else 'Neutral'))
```
### 4️⃣ Effectiveness Scoring

- Aggregate metrics by `drugName` and `condition`:
```python
effectiveness = df.groupby(['drugName', 'condition']).agg({
    'sentiment_score': 'mean',
    'rating': 'mean',
    'usefulCount': 'sum'
}).reset_index()
```
- Compute composite **Drug Effectiveness Index (DEI)**:
```python
df['DEI'] = 0.6*df['rating']/10 + 0.4*((df['sentiment_score']+1)/2)
```

### 5️⃣ Visualization

Generate visual insights:

- Top 10 most effective drugs by DEI.

- Word clouds for positive vs. negative feedback.

- Trend analysis of average rating over time.

- Correlation between `sentiment_score` and `rating`.

### 6️⃣ Power BI Dashboard

- Integrate processed CSV data for dynamic visualization (see dashboard spec below).
## 📊 Power BI Dashboard Preview – Drug Effectiveness Analysis

The report is designed for pharmaceutical analysts, clinical research teams, and healthcare data scientists to explore drug performance using real-world patient feedback.
### 🧭 Page 1 – Overview
🎯 Purpose

Give executives a quick snapshot of overall performance across all drugs, conditions, and patient reviews.<br />
📌 Recommended KPIs
| KPI                     | Description                                         |
| ----------------------- | --------------------------------------------------- |
| **Average Rating**      | Mean numerical patient rating for all drugs         |
| **Overall Sentiment %** | % of positive reviews across dataset                |
| **Review Volume**       | Total number of reviews                             |
| **Top Drug (by DEI)**   | Best-performing drug using Drug Effectiveness Index |
| **Most Reviewed Drug**  | Highest patient engagement                          |

### 📈 Recommended Visuals

- **KPI Cards**

  - Average Rating

  - Positive Sentiment %

  - Total Reviews

  - Avg DEI

- **Bar Chart:** Top 10 Drugs by DEI

- **Line Chart:** Review Volume Over Time

- **TreeMap:** Reviews by Condition

- **Matrix Table:** Drug × Condition × Avg DEI

### 🧠 Insights

- Identify which drugs are performing best overall.

- See which conditions have most patient feedback.

- Spot rising patient-reported issues based on temporal trends.

## 🎭 Page 2 – Sentiment Insights
### 🎯 Purpose

Explore emotional tone of patient reviews.

### 📌 KPIs

- Positive Sentiment %

- Negative Sentiment %

- Neutral Sentiment %

- Avg Sentiment Score (0–1 scaled)

### 📈 Recommended Visuals

- **Donut Chart:** Sentiment Breakdown

- **Stacked Bar:** Sentiment by Drug

- **Bar Chart:** Sentiment by Condition

- **Word Clouds:**

   - Positive Feedback

  - Negative Feedback

- **Scatter Plot:** Sentiment Score vs Rating

### 🧠 Insights

- Surface emotional patterns behind ratings.

- Identify which drugs trigger negative keywords (e.g., “nausea,” “fatigue,” “anxiety”).

- Compare emotional profiles of drugs used for the same condition.

## 🩺 Page 3 – Effectiveness by Condition
### 🎯 Purpose

Compare drug performance within the same medical condition to identify the most effective treatment options.

### 📌 KPIs

- Avg DEI (Drug Effectiveness Index) per Condition

- Best Drug for Each Condition

- Lowest-Performing Drug for Each Condition

### 📈 Recommended Visuals

- **Line Chart:** DEI Trend Over Time by Condition

- **Clustered Bar Chart:** Avg DEI by Drug (per selected condition)

- **Table:**
 - Drug

 - Avg DEI

 - Avg Rating

 - Avg Sentiment Score

- **Filter Panel:**

 - Condition

 - Gender

 - Age group

### 🧠 Insights

- Identify treatment differences for specific conditions.

- Detect demographic variation in drug effectiveness (optional feature).

- Understand long-term condition-specific trends.

  

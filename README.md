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

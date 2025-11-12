# 🛒 Flipkart Customer Support CSAT Prediction

**Project Goal:**  
Predict customer satisfaction (CSAT) from Flipkart customer support data using data cleaning, feature engineering, and machine learning models.

---

## 📘 Project Overview

Customer experience is critical for any e-commerce platform.  
This project analyzes Flipkart’s customer support data to identify the key drivers of satisfaction and build a predictive model that classifies whether a customer is **Satisfied (CSAT ≥ 4)** or **Unsatisfied (CSAT < 4)** based on support interaction details.

---

## 🧭 Workflow Summary

### 1. Data Understanding
- Dataset: `Customer_support_data.csv`
- Columns include issue timestamps, handling durations, item prices, customer remarks, agent details, and CSAT scores.

### 2. Data Cleaning
- Trimmed inconsistent column names and removed unnecessary whitespace.
- Converted time-related columns (`Issue Reported At`, `Issue Responded At`, `Connected Handling Time`) into standard datetime formats.
- Handled missing values through median imputation or dropped columns with >50% nulls.

### 3. Feature Engineering
- Derived `response_time_mins` (issue-to-response duration).
- Extracted text-based features from `Customer Remarks`:
  - Character length
  - Word count
  - Keyword indicators (refund, broken, delayed, etc.)
- Converted price and tenure features to numeric scales.

### 4. Exploratory Data Analysis (EDA)
- Visualized CSAT distribution.
- Checked correlations between satisfaction and features like response time and remark length.
- Identified imbalance in satisfaction labels (approx. 70% satisfied vs. 30% unsatisfied).

### 5. Modeling
- **Baseline Models:** Logistic Regression, Random Forest  
- **Balanced Model:** Applied **SMOTE** oversampling + `class_weight='balanced'` to handle class imbalance.

### 6. Evaluation
| Model | Accuracy | Recall (Unsatisfied) | Recall (Satisfied) | F1 Macro |
|--------|-----------|----------------------|--------------------|----------|
| Baseline Random Forest | 0.79 | 0.20 | 0.92 | 0.56 |
| Balanced (SMOTE) Random Forest | 0.77 | 0.35 | 0.85 | 0.60 |

✅ **SMOTE improved minority-class recall from 0.20 → 0.35**, making the model more fair and useful for identifying unhappy customers.

---

## 📊 Key Insights
- Faster response times are strongly linked to higher satisfaction.
- Customers mentioning keywords like *“refund”*, *“broken”*, or *“delayed”* are significantly more likely to leave lower CSAT scores.
- Balanced models help detect unsatisfied customers even if overall accuracy slightly drops.

---

## 🧠 Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Data Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn |
| ML Modeling | scikit-learn, imbalanced-learn, xgboost |
| Environment | Jupyter Notebook (Anaconda) |

---

## 📈 Results Summary
1. Accuracy: 77%.
2. Minority-class recall: 35%.
3. F1-macro: 0.60.
4. Balanced model effectively improves fairness by detecting low-CSAT cases more reliably.

---

## Next Steps
1. Experiment with NLP embeddings (TF-IDF or BERT) for remark sentiment.
2. Tune hyperparameters with Bayesian search for improved recall.
3. Deploy model as a Flask API for real-time CSAT prediction.

---


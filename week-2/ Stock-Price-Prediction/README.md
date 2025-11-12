# 📈 Stock Price Prediction — Apple (AAPL)

### 🗓️ Machine Learning Regression Assignment

## Objective
The goal of this project is to predict the **closing stock price** of Apple Inc. (AAPL) using historical data.  
This project demonstrates how regression models can be applied to real-world financial data to identify relationships and make predictive insights.

---

## 🧠 Key Concepts
- **Regression Modeling**
- **Feature Selection (SelectKBest, RFE)**
- **Model Evaluation (MAE, RMSE, R²)**
- **Data Preprocessing & Scaling**
- **Model Comparison (Linear, Lasso, Random Forest)**

---

## 📊 Dataset
The dataset was downloaded from **Yahoo Finance** and contains **5 years** of historical daily stock data for AAPL.  
It includes:
- `Date` – Trading day  
- `Open` – Opening price  
- `High` – Highest price of the day  
- `Low` – Lowest price of the day  
- `Close` – Price at market close *(Target Variable)*  
- `Volume` – Number of shares traded  

No missing values were present after cleaning.

---

## 🔍 Exploratory Data Analysis (EDA)
Performed EDA to understand data trends and relationships:
- **Line Chart:** Trend of closing prices over time.  
- **Heatmap:** Correlation between numeric features.  
- **Scatter Plots:** `Open`, `High`, and `Volume` vs. `Close` price.  

📌 *Visual insights show strong linear relationships between opening, high, low, and closing prices.*

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Cleaned and formatted dataset.
- Split data into 80% training and 20% testing sets.
- Scaled features using `StandardScaler` for linear models.

### 2. Feature Selection
- Used `SelectKBest` (f_regression) to score importance of features.
- Applied `RFE` (Recursive Feature Elimination) to find top predictors.

### 3. Models Implemented
| Model | Description |
|--------|--------------|
| Linear Regression | Baseline regression model |
| Lasso Regression | Linear model with L1 regularization |
| Random Forest Regressor | Ensemble-based regression for non-linear patterns |

### 4. Model Evaluation
Evaluated using:
- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**
- **R² (Coefficient of Determination)**

---

## 🧾 Results Summary

| Model | MAE | RMSE | R² |
|--------|------|------|------|
| Linear Regression | 0.80 | 1.07 | 0.999 |
| Lasso Regression | 0.93 | 1.21 | 0.999 |
| Random Forest | 1.09 | 1.52 | 0.998 |

✅ **Linear Regression** performed best — due to strong linear correlations among price features.

---

## 📉 Visualizations
The following visualizations were created:
1. **Closing Price Trend Over Time**
2. **Feature Correlation Heatmap**
3. **Model Comparison (R² Score)**
4. **Residual Analysis — Linear Regression**

*(Plots available in project notebook and report.)*

---

## 💡 Insights & Conclusion
- Linear relationships dominate short-term stock price features.  
- Random Forest and Lasso models also performed strongly but did not outperform Linear Regression.  
- In real-world forecasting, incorporating **time-series models (ARIMA, LSTM)** or **external data** such as news sentiment would enhance realism.

---

## 🧰 Tools & Libraries
- Python 3.11  
- pandas, numpy, matplotlib, seaborn  
- scikit-learn (LinearRegression, Lasso, RandomForestRegressor, SelectKBest, RFE)

---

## 🏁 Conclusion
This project demonstrates the application of regression models in financial forecasting using stock data.  
It highlights data cleaning, feature selection, and model evaluation, fulfilling the **Week 2 Machine Learning Regression** assignment objectives.

---

### Author
**Shivali Muthukumar | Data Analyst**  

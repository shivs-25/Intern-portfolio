#!/usr/bin/env python
# coding: utf-8

# In[82]:


# Stock Price Prediction — Apple (AAPL)

## Introduction:
# The goal of this project is to predict the closing price of Apple Inc. (AAPL) stock using historical market data.  
# Stock price prediction is important for investors, analysts, and researchers in finance as it helps in decision-making and understanding market dynamics.  

# I have applied machine learning regression techniques(Linear Regression, Lasso, Random Forest) to build predictive models.  
# I have also performed feature selection and evaluate models using error metrics (MAE, RMSE) and accuracy (R² score).


# In[84]:


print("Step 1: Import the necessary libraries\n")

import pandas as pd  # For data handling and analysis.
import numpy as np   # For numerical operations.
import matplotlib.pyplot as plt  # For data visualizations.
import seaborn as sns  # For advanced visualizations.

# Machine learning models and feature selection tools

from sklearn.linear_model import LinearRegression, Lasso  # Linear and Lasso Regression models.
from sklearn.feature_selection import SelectKBest, f_regression, RFE  # Feature selection methods.
from sklearn.ensemble import RandomForestRegressor  # Random Forest Model.

# Tools to split dataset and scale features

from sklearn.model_selection import train_test_split  # For splitting data.
from sklearn.preprocessing import StandardScaler  # For scaling features.

# Metrics to evaluate how well models perform

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# In[89]:


print("Step 2: Load and display first 5 rows of dataset\n")

df = pd.read_csv("AAPL.csv")

# Rename columns
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]

# Drop rows where 'Open' is not numeric (removes the 'AAPL' junk row)
df = df[pd.to_numeric(df["Open"], errors="coerce").notnull()]

# Convert all numeric columns properly
for col in ["Open", "High", "Low", "Close", "Volume"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.head())
print("Dataset shape:", df.shape)


# In[90]:


print("Step 3: Check for missing values\n")
print("Missing values per column:")
print(df.isnull().sum())

# In our case, all columns have 0 missing values, so no cleaning needed


# In[87]:


## Dataset Description
# The dataset contains historical daily stock prices of Apple (AAPL).  

# The columns are:

# - Date: Trading day (not used in modeling).  
# - Open: Price at the start of trading.  
# - High: Highest price of the day.  
# - Low: Lowest price of the day.  
# - Close: Price at market close (Prediction target).  
# - Volume: Number of shares traded.  

# The dataset contains 1256 rows covering approximately 5 years of data.  
# No missing values were found in the dataset.


# In[92]:


# Exploratory Data Analysis (EDA)

# Drop the Date column since it's not numeric and not needed
df = df.drop(columns=["Date"])

# 1. Plot Closing Price over time
plt.figure(figsize=(10,5))
plt.plot(df["Close"], label="Close Price")
plt.title("AAPL Closing Price Over Time")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# 2. Correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()


# In[109]:


print("Additional EDA: Scatter plots to visualize relationships with Close price\n")

print("a. Volume VS Close Price:\n")
plt.figure(figsize=(6,4))
plt.scatter(df["Volume"], df["Close"], alpha=0.5)
plt.title("Volume vs Close Price")
plt.xlabel("Volume")
plt.ylabel("Close Price")
plt.show()

print("b. Open VS Close Price:\n")
plt.figure(figsize=(6,4))
plt.scatter(df["Open"], df["Close"], alpha=0.5, color="g")
plt.title("Open vs Close Price")
plt.xlabel("Open Price")
plt.ylabel("Close Price")
plt.show()

print("c. High VS Close Price:\n")
plt.figure(figsize=(6,4))
plt.scatter(df["High"], df["Close"], alpha=0.5, color="r")
plt.title("High vs Close Price")
plt.xlabel("High Price")
plt.ylabel("Close Price")
plt.show()

print("\nStatistical Summary:\n",df.describe())


# In[95]:


print("Step 4: Prepare features and target\n")

# Define features (inputs) and target (output)
features = ["Open", "High", "Low", "Volume"]   # Independent variables
target = "Close"                               # Dependent variable

X = df[features]   # Feature matrix
y = df[target]     # Target vector

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)


# In[96]:


print("Step 5: Split dataset into training and testing sets\n")

from sklearn.model_selection import train_test_split

# Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)


# In[97]:


print("Step 6: Feature Scaling (important for Linear/Lasso models)\n")

# Create a scaler
scaler = StandardScaler()

# Fit scaler on training data, transform both train and test
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling complete — features now normalized")


# In[98]:


print("Step 7: Feature Selection with SelectKBest (f_regression)\n")

selector = SelectKBest(score_func=f_regression, k="all")  # score all features
selector.fit(X_train_scaled, y_train)

print("Feature scores:")
for feature, score in zip(features, selector.scores_):
    print(f"{feature}: {score:.2f}")


# In[99]:


print("Step 8: Feature Selection with RFE (Recursive Feature Elimination)\n")

lin_reg = LinearRegression()
rfe = RFE(estimator=lin_reg, n_features_to_select=2)  # select 2 best features
rfe.fit(X_train_scaled, y_train)

print("Selected Features (RFE):", [f for f, keep in zip(features, rfe.support_) if keep])


# In[100]:


## Methodology
# 1. Data Preprocessing: 
   # - Loaded historical Apple stock data.  
   # - Cleaned dataset by fixing headers and dropping irrelevant rows.  
   # - Checked for missing values (none found).  

# 2. Feature Selection: 
   # - Applied `SelectKBest` to score features.  
   # - Applied `RFE` (Recursive Feature Elimination) to identify most important predictors.  

# 3. Models Used: 
   # - Linear Regression — baseline model.  
   # - Lasso Regression — regression with L1 regularization (shrinks coefficients).  
   # - Random Forest Regressor — ensemble model for improvement, handles non-linearities.  

# 4. Evaluation Metrics: 
   # - MAE (Mean Absolute Error).
   # - RMSE (Root Mean Squared Error).
   # - R² Score (Coefficient of Determination).


# In[101]:


print("Step 9: Train and evaluate models\n")

# Function to train and evaluate a model
def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)                # Train model
    y_pred = model.predict(X_test)             # Predict on test set

    mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
    mse = mean_squared_error(y_test, y_pred)   # Mean Squared Error
    rmse = np.sqrt(mse)                        # Root Mean Squared Error
    r2 = r2_score(y_test, y_pred)              # R² Score

    print(f"\n📊 {name} Results:")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²: {r2:.2f}")
    print("-"*30)

    return [name, mae, rmse, r2]

results = []

# Linear Regression
results.append(evaluate_model("Linear Regression", LinearRegression(),
                              X_train_scaled, X_test_scaled, y_train, y_test))

# Lasso Regression
results.append(evaluate_model("Lasso Regression", Lasso(alpha=0.01),
                              X_train_scaled, X_test_scaled, y_train, y_test))

# Random Forest (does not need scaling)
results.append(evaluate_model("Random Forest", RandomForestRegressor(n_estimators=100, random_state=42),
                              X_train, X_test, y_train, y_test))


# In[102]:


print("Model Improvement: Hyperparameter tuning for Random Forest\n")

from sklearn.model_selection import GridSearchCV

# Define parameter grid for Random Forest
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10, None]
}

grid = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1
)

# Fit on training data
grid.fit(X_train, y_train)

print("Best Parameters (Random Forest):", grid.best_params_)
print("Best CV R² Score:", grid.best_score_)

# Evaluate tuned model on test set
y_pred_tuned = grid.best_estimator_.predict(X_test)
print("Test R² (Tuned Random Forest):", r2_score(y_test, y_pred_tuned))


# In[103]:


print("Step 10: Compare results in a table\n")

results_df = pd.DataFrame(results, columns=["Model", "MAE", "RMSE", "R²"])
print(results_df)


# In[104]:


print("Residual Analysis for Linear Regression\n")

# Train Linear Regression again on scaled data
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)
y_pred = lin_reg.predict(X_test_scaled)

# Compute residuals (difference between actual and predicted)
residuals = y_test - y_pred

plt.figure(figsize=(6,4))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Predicted Close Price")
plt.ylabel("Residuals")
plt.title("Residual Analysis - Linear Regression")
plt.show()


# In[105]:


## Results:

#All models performed extremely well on the dataset:

# - Linear Regression achieved R² ≈ 0.999, showing an almost perfect fit.  
# - Lasso Regression also performed very well, but slightly lower than Linear Regression because of coefficient shrinkage.  
# - Random Forest performed strongly with R² ≈ 0.998, though it did not outperform the simple Linear Regression.

# This is expected because Open, High, Low, and Close prices are highly correlated.  
# Stock market data within the same day shows strong linear relationships, which explains why Linear Regression is so effective here.


# In[106]:


print("Step 11: Plot model comparison (R² score)\n")

plt.figure(figsize=(8,5))
sns.barplot(x="Model", y="R²", data=results_df)
plt.title("Model Comparison (R² Score)")
plt.show()


# In[107]:


## Conclusion:

# In this project, we successfully predicted Apple’s stock closing price using historical data.  
# We compared Linear Regression, Lasso, and Random Forest models:

# - All models achieved high accuracy (R² > 0.99).  
# - Linear Regression** was sufficient for this dataset because of the strong linear correlations between stock prices.  
# - Random Forest provided a robust alternative but did not show significant improvement.  

### Future Work:

# To make predictions more realistic in real-world trading, we could include:
# - External features such as news sentiment, market indices, and macroeconomic indicators.  
# - Longer-term datasets to detect seasonality and trends.  
# - Time-series models like ARIMA, LSTM (deep learning) for sequential forecasting.

# This demonstrates that Machine Learning Regression models can effectively capture stock price relationships but real-world forecasting requires richer features.


# In[ ]:





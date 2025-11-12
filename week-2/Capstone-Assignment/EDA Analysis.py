#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit


# In[95]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import streamlit as st


# In[38]:


print("Load Dataset\n")

df = pd.read_csv("/Users/shivalimuthukumar/Desktop/mydrive/AmesHousing.csv")
df.shape


# In[39]:


print("Selecting Numbered Columns\n")

df_no = df.select_dtypes(include = [np.number])

df_no.shape


# In[40]:


df_no.head()


# In[41]:


df_no.columns


# In[42]:


# SalePrice is dependent variable and all the others are independent variables
# Check how the independent variables are co-reled with the dependent variable (SalePrice)
# Variables that are strongly co-related to SalePrice will be retained as columns.
# Ones that are not strongly co-related will be eliminated.


# In[44]:


print("Finding Correlation matrix\n")

corr_matrix = df_no.corr()


# In[45]:


corr_with_sale_price = corr_matrix[['SalePrice']].sort_values(by = 'SalePrice', ascending = False)
print(corr_with_sale_price)


# In[47]:


# Correlations of variables that are greater than the average correlation will be slected (top 10).
# Ones that do not satisfy this condition will be eliminated.

print("Calculating the average of the correlations obtained\n")

corr_with_sale_price_updated = corr_matrix['SalePrice'].drop('SalePrice') # cannot take the dependent variable while calculating average.


# In[48]:


print("Calculating mean correlation\n")

mean_corr = corr_with_sale_price_updated.mean()
print("The mean correlation of all independent variables with SalePrice is: ", mean_corr)


# In[50]:


print("Setting a threshold for correlation\n")
threshold = mean_corr # All variables having a correlation above the threshold of the mean correlation will be considered.

print("Find columns where the absolute correlation with SalePrice is less than the threshold\n")
low_corr_columns = corr_matrix['SalePrice'].abs() < threshold

print("Dropping these columns from the dataset\n")
df_cleaned = df_no.drop(columns = corr_matrix.columns[low_corr_columns])

print("Columns have been dropped successfully!")


# In[51]:


print("Displaying the remaining columns\n")
print("Columns with significant correlation to SalePrice:\n")
print(df_cleaned.columns)


# In[52]:


df_cleaned.columns


# In[53]:


df_cleaned.shape


# In[54]:


print("Finding null values\n")

df_cleaned.isnull().sum()


# In[55]:


df_cleaned = df_cleaned.dropna(subset = ['Lot Frontage','Mas Vnr Area','BsmtFin SF 1','Total Bsmt SF','Bsmt Full Bath','Garage Yr Blt','Garage Cars','Garage Area'])

print("Null values have been removed!")
print("Data Cleaning and Pre-processing have been successfully completed!")


# In[56]:


print("Feature Engineering\n")

print("Defining features and the target variable\n")
x = df_cleaned.drop('SalePrice', axis = 1)
y = df_cleaned['SalePrice']

print("Features and Target successfully defined!")


# In[57]:


print("1. Correlation Analysis\n")

corr_matrix = df_cleaned.corr()
corr_with_saleprice = corr_matrix['SalePrice'].drop('SalePrice').abs()
print("Correlation with SalePrice:\n")
print(corr_with_saleprice.sort_values(ascending = False))


# In[64]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import matplotlib.pyplot as plt


# In[61]:


print("2. Univariate Feature Selection\n")
print("Univariate Feature Selection (SelectKBest): ")
selector = SelectKBest(score_func = f_regression, k = 10)
selector.fit(x,y)
selected_features_univariate = x.columns[selector.get_support()]
print(selected_features_univariate)


# In[65]:


print("3. Recursive Feature Elimination (RFE)\n")

print("Recursive Feature Elimination (RFE):")
model_rfe = LinearRegression()
rfe = RFE(estimator = model_rfe, n_features_to_select = 10)
rfe.fit(x,y)
selected_features_rfe = x.columns[rfe.support_]
print(selected_features_rfe)


# In[68]:


print("4. Lasso Regularization\n")

print("Lasso Regularization:")
lasso = Lasso(alpha = 0.01)
lasso.fit(x,y)
selected_features_lasso = x.columns[lasso.coef_!=0]
print(selected_features_lasso)


# In[69]:


print("5. Tree-Based Feature Importance\n")

print("Tree-Based Feature Importance (Random Forest):")
rf = RandomForestRegressor()
rf.fit(x,y)
importances = rf.feature_importances_
importance_df = pd.DataFrame({"Feature" : x.columns, 'Importance' : importances})
top_features_rf = importance_df.sort_values(by = 'Importance', ascending = False).head(10)
print(top_features_rf)


# In[71]:


print("Visualizing the feature importance from Random Forest\n")

plt.figure(figsize = (10,6))
sns.barplot(x = 'Importance', y = 'Feature', data = top_features_rf)
plt.title("Top 10 Feature Importance from Random Forest")
plt.show()


# In[72]:


print("Finding common features across all methods\n")
common_features = selected_features_univariate.intersection(selected_features_rfe).intersection(selected_features_lasso)

print("Common features across all methods:")
print(common_features)


# In[80]:


print("Combining all methods to find the common features\n")

common_features = (
            selected_features_univariate
            .intersection(selected_features_rfe)
            .intersection(selected_features_lasso)
            .intersection(top_features_rf) # include Random Forest feature importance
)

print("Displaying Common Features\n")
print("Common Features across all methods (including Random Forest): ")
print(common_features)


# In[83]:


type(top_features_rf)


# In[88]:


print("Creating a DatFrame only with the Common Features.\n")

common_features_list = list(common_features)  # convert set to list
common_features_list.append("SalePrice") # Include SalePrice as well
df_common = df_cleaned[common_features_list]
print("DataFrame with the updated features")


# In[89]:


print("DataFrame with Common Features:")
print(df_common.head())


# In[90]:


print("Define features and target variable for common features\n")
x_common = df_common.drop('SalePrice', axis = 1)
y_common = df_common['SalePrice']


# In[91]:


print("Splitting the Data into Training and Testing sets\n")
x_train, x_test, y_train, y_test = train_test_split(x_common, y_common, test_size = 0.2, random_state = 42)


# In[96]:


print("Initializing Models\n")
models = {
    'Linear Regression' : LinearRegression(),
    'Lasso Regression' : Lasso(alpha=0.01),
    'Random Forest' : RandomForestRegressor(random_state = 42),
    'Gradient Boosting' : GradientBoostingRegressor(random_state = 42),
    'XGBoost' : XGBRegressor (objective = 'reg:squarederror' , random_state = 42)
}


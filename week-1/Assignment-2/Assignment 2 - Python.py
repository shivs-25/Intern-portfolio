#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


# Loading dataset

b_cancer = load_breast_cancer()

# Creating DataFrame

df_cancer = pd.DataFrame(b_cancer.data, columns = b_cancer.feature_names)
df_cancer["target"] = b_cancer.target


# In[8]:


# Showing first 5 rows

df_cancer.head()


# In[9]:


# Showing Shape of Dataset

df_cancer.shape


# In[10]:


# Showing Data types

df_cancer.info()


# In[11]:


# Statistical Summary

df_cancer.describe()


# In[12]:


# Mean, Median, Std of mean radius

df_cancer["mean radius"].mean(), df_cancer["mean radius"].median(), df_cancer["mean radius"].std()


# In[13]:


# Missing Values

df_cancer.isnull().sum()


# In[14]:


print("Data Cleaning\n")

df_cancer["target"].value_counts()


# In[15]:


print("Descriptive Statistics\n")

df_cancer[["mean area","mean compactness"]].agg(["mean","median","std"])


# In[16]:


print("Histograms for mean radius\n")

df_cancer["mean radius"].hist(bins = 30, figsize = (6,4))
plt.xlabel("Mean Radius")
plt.ylabel("Frequency")
plt.title("Histogram of Mean Radius")
plt.show()


# In[17]:


print("Boxplot for mean texture\n")

sns.boxplot(x=df_cancer["mean texture"])
plt.title("Boxplot of Mean Texture")
plt.show()


# In[18]:


print("Calculating IQR\n")

Q1 = df_cancer["mean texture"].quantile(0.25)
Q3 = df_cancer["mean texture"].quantile(0.75)
IQR = Q3 - Q1
IQR


# In[20]:


df_cancer.groupby("target")["mean perimeter"].mean()


# In[22]:


# Data Visualisation

print("Bar Chart for Benign vs Maignant\n")
df_cancer["target"].value_counts().plot(kind="bar")
plt.xticks([0,1], ["Malignant (0)", "Benign (1)"])
plt.title("Benign vs Malignant Cases")
plt.show()


# In[24]:


print("Scatter Plot for Mean radius vs Mean texture\n")

plt.scatter(df_cancer['mean radius'], df_cancer["mean texture"], c = df_cancer["target"])
plt.xlabel("Mean Radius")
plt.ylabel("Mean Texture")
plt.title("Mean Radius vs Mean Texture")
plt.show()


# In[25]:


print("Pairplot\n")

sns.pairplot(df_cancer[["mean radius", "mean texture", "mean perimeter", "mean area", "target"]], hue = "target")
plt.show()


# In[26]:


print("Heatmap Correlation\n")

plt.figure(figsize = (12,8))
sns.heatmap(df_cancer.corr(), cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# In[29]:


print("Feature Engineering\n")

#creating new feature, area-to-perimeter-ratio

df_cancer["area_to_perimeter_ratio"] = df_cancer["mean area"] / df_cancer["mean perimeter"]

#Comparing between benign/malignant

df_cancer.groupby("target")["area_to_perimeter_ratio"].mean()

# Another feature, radius_to_texture_ratio

df_cancer["radius_to_texture_ratio"] = df_cancer["mean radius"] / df_cancer["mean texture"]

# Comparing new features between groups

df_cancer.groupby("target")["radius_to_texture_ratio"].mean()


# In[30]:


print("Conclusion:\n")

print("1. The breast cancer dataset has 569 rows and 31 features.\n")
print("2. No missing values were found in this dataset.\n")
print("3. Mean radius, mean area and mean perimeter show big differences between Benign and Malignant.\n")
print("4. Visualization shows Benign and Malignant cases are separable by radius/texture.\n")
print("5. Correlation Heatmap shows strong correlations between size-related features.\n")
print("6. Newly engineered features such as, area_to_perimeter_ratio and radius_to_texture_ratio, help see the differences.")


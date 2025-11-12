#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from statistics import mean, median, mode, variance, stdev
from scipy.stats import norm


# In[2]:


print("1. Mean, Median and Mode\n")
data = [12,15,12,14,19,16,18,12,16,15]
print("Mean: ", mean(data))
print("Median: ", median(data))
print("Mode: ", mode(data))


# In[3]:


print("2. Variance and Standard Deviation\n")

scores = [45,55,65,75,85,95,100,85,90,75]
print("Variance: ", variance(scores)) #sample variance
print("Standard Deviation: ", stdev(scores))


# In[4]:


print("3. Range and IQR\n")

sales = [50,60,55,65,60,70]
print("Range: ", max(sales) - min(sales))

Q1 = np.percentile(sales, 25)
Q3 = np.percentile(sales, 75)
IQR = Q3 - Q1
print("IQR: ", IQR)


# In[5]:


print("4. Probability\n")

A, B, C = 40, 35, 25
total = A + B + C
print("Probability of B: ", B/total)


# In[9]:


print("5. Normal Distribution\n")

mean_height = 170
std_dev = 10
x = 180
prob = 1 - norm.cdf(x, mean_height, std_dev)
print("P(Height > 180): ", prob)


# In[ ]:





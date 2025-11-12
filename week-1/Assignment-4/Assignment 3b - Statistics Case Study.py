#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# CASE 1 - Teaching Methods vs Exam Scores

g1 = np.array([65,70,75,80,85,78,82,79,74,68,72,77,71,84,73])  # Traditional
g2 = np.array([58,62,67,65,69,70,64,60,66,68,71,59,63,67,61])  # Online
g3 = np.array([75,78,80,85,87,82,79,88,83,81,85,84,89,86,80])  # Blended


# In[3]:


print("1. Descriptive Statistics\n")

def describe(x):
    return {
        "mean": x.mean(),
        "median": np.median(x),
        "std": x.std(ddof = 1)
    }

print("G1 (Traditional): ", describe(g1))
print("G2 (Online): ", describe(g2))
print("G3 (Blended): ", describe(g3))


# In[14]:


print("One-way ANOVA (alpha = 0.05)\n")

f_stat, p_val = stats.f_oneway(g1, g2, g3)
print("ANOVA: F =", round(f_stat, 3), "p =", p_val)

print("\np-value < 0.05, there is significant difference among groups.")


# In[9]:


print("3. Post-hoc: Tukey's HSD\n")

scores = np.r_[g1, g2,g3]
labels = (["Traditional"]*len(g1) +
          ["Online"] * len(g2) +
          ["Blended"] * len(g3))

tukey = pairwise_tukeyhsd(endog = scores, groups = labels, alpha = 0.05)
print(tukey)


# In[13]:


print("4. Assumptions\n")

print("\nShapiro-Wilk (normality) for each group:\n")

print("Shapiro G1: ", stats.shapiro(g1))
print("Shapiro G2: ", stats.shapiro(g2))
print("Shapiro G3: ", stats.shapiro(g3))

print("\nLevene (equal variances):\n")

lev_stat, lev_p = stats.levene(g1, g2, g3, center = "median")
print("Levene: stat =", round(lev_stat,3), "p =", lev_p)


# In[23]:


print("Conclusions\n")

print("a. We compared student scores across three teaching methods: Traditional, Online, and Blended.\n")
print("b. Descriptive statistics showed that the Blended method had the highest average scores, followed by Traditional, and Online had the lowest.\n")
print("c. ANOVA confirmed that the differences in means were statistically significant (p < 0.05).\n")
print("d. Post-hoc (Tukey) tests showed that Blended scores were significantly higher than Online, and also higher than Traditional. Online was significantly lower than both Blended and Traditional.\n")
print("e. Assumptions (normality and equal variances) were reasonably satisfied, so results are valid.\n")

print("\nThe Blended teaching method leads to significantly higher exam scores compared to both Traditional and Online methods. Online teaching alone produced the lowest results. This suggests that a Blended approach is the most effective method for improving student performance.\n")


# In[17]:


# CASE 2 - Marketing Campaign vs Sales


# In[18]:


north = np.array([102,110,108,104,112,109,115,114,120,118,107,113,117,121,116,111,119,122,125,126])
south = np.array([95,100,98,102,97,101,104,105,108,106,99,103,107,109,110,98,102,108,105,107])
west  = np.array([110,115,120,125,123,119,121,124,127,130,118,126,129,128,131,117,122,128,132,134])

print("1. Descriptive Statistics.\n")

def describe(x):
    return {"mean": x.mean(), "median": np.median(x), "std": x.std(ddof=1)}

print("North:", describe(north))
print("South:", describe(south))
print("West: ", describe(west))


# In[19]:


print("2. One-way ANOVA.\n")

f_stat, p_val = stats.f_oneway(north, south, west)
print("ANOVA: F =", round(f_stat,3), "p =", p_val)


# In[20]:


print("Tukey post-hoc\n")

sales = np.r_[north, south, west]
labels = (["North"]*len(north) + ["South"]*len(south) + ["West"]*len(west))
tukey = pairwise_tukeyhsd(endog=sales, groups=labels, alpha=0.05)
print(tukey)


# In[21]:


print("Assumptions\n")

print("\nShapiro–Wilk (normality)\n")
print("Shapiro North:", stats.shapiro(north))
print("Shapiro South:", stats.shapiro(south))
print("Shapiro West :", stats.shapiro(west))

print("\nLevene (equal variances)\n")
lev_stat, lev_p = stats.levene(north, south, west, center='median')
print("Levene: stat =", round(lev_stat,3), "p =", lev_p)


# In[22]:


print("One-sample t-tests vs 110(two-sided).\n")

def one_sample_test(x, mu=110):
    t, p = stats.ttest_1samp(x, popmean=mu)
    return {"t": t, "p_two_tailed": p, "mean": x.mean()}

print("North vs 110: ", one_sample_test(north))
print("South vs 110: ", one_sample_test(south))
print("West vs 110: ", one_sample_test(west))


# In[24]:


print("Conclusions\n")

print("a. We compared average sales across North, South, and West regions.\n")
print("b. Descriptive statistics showed that the West region had the highest mean sales, North was in the middle, and South had the lowest.\n")
print("c. ANOVA showed that the differences in sales across regions were statistically significant (p < 0.05).\n")
print("d. Post-hoc (Tukey) confirmed that the West region’s sales were significantly higher than both North and South, while South was significantly lower.\n")
print("e. One-sample t-tests compared each region’s mean to the company’s target of $110,000: 1. North: close to 110k, not significantly different, 2. South: significantly below 110k and 3. West: significantly above 110k.\n")
print("f. Assumptions were satisfied, so results are reliable.\n")

print("\nThe West region’s marketing campaign is the most successful, consistently achieving sales above the $110,000 target and significantly outperforming North and South. The South region is underperforming compared to the target. The company should focus on expanding the West campaign strategy and investigate the reasons for South’s weaker performance.\n")


# In[ ]:





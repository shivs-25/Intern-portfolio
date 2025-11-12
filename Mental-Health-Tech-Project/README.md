# 🧠 Mental Health in Tech – Exploratory Data Analysis (EDA)

## Overview
This project investigates patterns of **mental health and workplace support in the technology industry**, using the *2014 OSMI Mental Health in Tech Survey*.  
The goal is to identify demographic trends, work environment factors, and employer policies associated with mental health outcomes and attitudes.

The project was completed as an academic EDA assignment and is fully reproducible, with all code, outputs, and interpretations in a single Jupyter notebook.

---

## Objectives
1. **Data Understanding & Cleaning**
   - Standardize variables (`Gender`, `Age` filtering 18–100)
   - Handle missing values systematically
   - Drop irrelevant text or timestamp columns

2. **Univariate & Bivariate Analysis**
   - Explore distributions of demographic and workplace factors
   - Examine associations between mental health treatment, gender, and work interference
   - Assess benefits, anonymity, and company size relationships

3. **Attitudinal and Organizational Insights**
   - Measure comfort discussing mental health
   - Compare perceptions of mental vs physical health seriousness
   - Evaluate cultural and geographic differences

4. **Predictive Insights**
   - Encode categorical variables and visualize correlations
   - Optional logistic regression predicting treatment seeking

5. **Actionable Recommendations**
   - Derive organizational and policy suggestions based on the evidence

---

## Key Findings (from the final executed notebook)
- **Sample:** 1,251 respondents (median age 31 years, IQR 9).  
- **Gender distribution:** 79.1% Male, 20.1% Female, 0.8% Other — highlighting representation gaps.  
- **Treatment prevalence:** 50.5% overall; the *Other* gender category reported the highest treatment rate (90%) vs *Male* (45.4%).  
- **Work interference:** 48.3% reported that mental health affected work performance.  
- **Geography:** Highest reported interference in Canada (55.6%), Germany (51.1%), and the U.S. (49.5%).  
- **Company size:** Benefits were most prevalent in firms with >1000 employees (64.8%) and least in 1–5 employee firms (10.8%).  
- **Remote work:** Differences in treatment and support access noted between remote and on-site respondents.  
- **Parity perceptions:** Discrepancies persist in how seriously mental health is treated compared to physical health, across gender and employer type.

---

## Recommendations
1. **Expand benefits access** in smaller companies with limited mental-health coverage.  
2. **Normalize discussions** through training and leadership modeling to reduce stigma.  
3. **Improve confidentiality** and data governance in non-tech contexts.  
4. **Ensure parity for remote employees** in access to care and well-being initiatives.  
5. **Integrate mental-health KPIs** alongside physical health metrics for organizational accountability.

---

## Technologies Used
- **Python 3.11+**
- **Jupyter Notebook**
- **pandas**, **numpy**
- **matplotlib**
- **scikit-learn** (for optional logistic regression)
- **nbconvert** (for notebook execution and HTML export)

---

## Dataset Reference
Source: Open Sourcing Mental Illness (OSMI) – Mental Health in Tech Survey, 2014
Dataset available at https://osmihelp.org/research
The dataset is licensed for research and educational use. Attribution to OSMI is maintained.

---


# Bellabeat Fitness Data Analysis Project  

### 📊 A Complete Data Analytics Case Study Using SQL, Python (Pandas), and Tableau

---

## 🧭 Project Overview  

This project analyzes **Fitbit fitness tracker data** to uncover insights about user activity, calorie expenditure, and sleep habits.  
The analysis supports **Bellabeat**, a high-tech wellness company that manufactures health-focused smart devices for women,  
in understanding consumer usage patterns and improving data-driven product decisions.

---

## 🎯 Business Task  

To identify key trends and relationships in smart device usage data that can help Bellabeat:  
- Understand daily activity patterns and engagement levels  
- Correlate physical activity with calorie expenditure  
- Examine user sleep duration and consistency  
- Derive insights to support product and marketing strategies  

---

## 🧩 Dataset  

- **Source:** Fitbit Fitness Tracker Data (via Amazon Mechanical Turk, 2016)  
- **Duration:** April 12 – May 12, 2016  
- **Participants:** 33 unique users  
- **Files Used (18 CSVs):**
  - `dailyActivity_merged.csv`  
  - `dailyCalories_merged.csv`  
  - `dailyIntensities_merged.csv`  
  - `dailySteps_merged.csv`  
  - `sleepDay_merged.csv`  
  - `weightLogInfo_merged.csv`  
  - Hourly and minute-level datasets for deeper insights  

---

## 🛠️ Tools & Technologies  

| Tool | Purpose |
|------|----------|
| **SQL (SQLite)** | Data exploration & aggregation |
| **Python (Pandas, Matplotlib)** | Cleaning, transformation, EDA, correlation analysis |
| **Tableau Public** | Data visualization and dashboard creation |
| **Jupyter Notebook** | Python development environment |

---

## 🧹 Data Cleaning Steps (Python / Pandas)

1. Standardized date formats to `YYYY-MM-DD`.  
2. Removed duplicate and zero-value entries.  
3. Merged datasets (`dailyActivity`, `sleepDay`, `weightLogInfo`) on `Id` and `ActivityDate`.  
4. Handled nulls and inconsistent IDs.  
5. Saved cleaned dataset as: cleaned_final_merged.csv.

---

## 🧮 SQL Analysis Highlights  

| Query | Description | Key Insight |
|--------|--------------|-------------|
| Count distinct users | Identified 33 unique participants | ✅ |
| Average steps & calories | Found avg. 11,000 steps/day | Users moderately active |
| Steps vs Calories correlation | r = 0.59 | Strong positive relationship |
| Sleep hours per user | Avg = 6.6 hours/day | Slightly below ideal rest |
| Activity by weekday | Peak on Tuesdays & Saturdays | Higher weekend activity |

---

## Python (Pandas) EDA Highlights  

- Correlation between Steps and Calories: **0.592**  
- Correlation between Very Active Minutes and Calories: **0.65**  
- Weak correlation between Sleep and Steps (−0.08)  

**Visualization Examples:**  
- Daily step trends (line chart)  
- Calories vs steps (scatter plot)  
- Sleep duration histogram  
- Correlation heatmap  

**Key Findings:**  
- High step count correlates with increased calorie burn.  
- Sedentary time negatively impacts active metrics.  
- Sleep duration averages ~6.6 hours with inconsistent patterns.  

---

## Tableau Dashboard  

**Dashboard Components:**
1. **Daily Total Steps Over Time** — Line chart showing activity trends  
2. **Calories vs Total Steps** — Scatter plot with trendline (R² = 0.326, p = 0.0005)  
3. **Sleep Duration Distribution** — Histogram of hours slept (avg = 6.6 hrs)  
4. **Correlation Heatmap** — Relationship matrix across metrics  


---

## 💡 Insights Summary  

| Area | Insight | Recommendation |
|-------|----------|----------------|
| **Activity Trends** | Avg 11,000 steps/day | Encourage weekday consistency |
| **Calories Burned** | Strong link with steps | Add step-based calorie goals |
| **Sleep Patterns** | Avg 6.6 hrs/day | Provide rest balance reminders |
| **Engagement** | Peaks on weekends | Launch weekend challenges |

---

## 🧠 Recommendations for Bellabeat  

1. **Personalized Activity Targets:** Encourage users with adaptive daily goals.  
2. **Rest Balance Alerts:** Detect imbalance between activity and recovery.  
3. **Weekend Engagement:** Push weekend badges and streak rewards.  
4. **Smart Sleep Coaching:** Provide AI-driven sleep improvement tips.  
5. **Trend Insights in App:** Visualize user’s personal correlations (steps ↔ sleep ↔ calories).  

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

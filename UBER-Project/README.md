# Uber Supply and Demand Gap Analysis

### Data Analytics | Excel | SQL | Python | Visualization

---

## **Project Overview**

This project analyzes **Uber ride request data** to identify patterns in supply and demand across time slots and pickup points.  
The goal is to understand where and when Uber faces major **supply-demand gaps** — such as unfulfilled requests due to driver unavailability or cancellations.

The dataset includes over **6,700 ride requests**, containing details such as:
- Request timestamps
- Drop timestamps
- Pickup locations (City / Airport)
- Request statuses (Trip Completed / Cancelled / No Cars Available)

---

## **Objectives**

- Identify when and where Uber faces maximum unmet demand.  
- Examine trip completion rates and driver availability trends.  
- Compare patterns between **City** and **Airport** pickups.  
- Recommend operational improvements to reduce unfulfilled requests.

---

## **Tools & Technologies**

| Tool | Purpose |
|------|----------|
| **Excel** | Data cleaning, preprocessing, dashboards |
| **SQLite (via Jupyter Notebook)** | SQL analysis & aggregations |
| **Python (Pandas, Matplotlib, Seaborn)** | Exploratory Data Analysis (EDA) |
| **VS Code / Jupyter Notebook** | Coding environment |
| **Google Docs / Word** | Final Insights Report |

---

## **Project Workflow**

### **1. Data Cleaning (Excel)**
- Removed invalid or missing values.  
- Converted timestamps to DateTime format.  
- Created helper columns for request hour and time slot.  
- Built an Excel dashboard for initial insights.

📄 **Output:** `Book1.pdf`

---

### **2. SQL Analysis (SQLite)**

Performed SQL-based aggregations to summarize requests by status, hour, and pickup point.

1. Example Queries:
   ```sql
   -- Total requests by status
   SELECT Status, COUNT(*) AS Total_Requests
   FROM uber_requests
   GROUP BY Status;

   -- Supply-demand gap percentage
   SELECT "Pickup point",
   COUNT(*) AS Total_Requests,
   SUM(CASE WHEN Status='Trip Completed' THEN 1 ELSE 0 END) AS Completed,
   ROUND(100.0 * SUM(CASE WHEN Status!='Trip Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS Gap_Percentage

   FROM uber_requests
   GROUP BY "Pickup point";

📄 **Output:** `Book1.pdf`

---

### ***3. Exploratory Data Analysis (Python)***
Conducted EDA using Pandas, Matplotlib, and Seaborn to visualize:
   - Request status distribution.
   - Pickup point performance.
   - Hourly supply-demand patterns.

📄 **Output:** 'Sample_EDA_Submission_Template.ipynb'

---

## **4. Insights and Findings**
### Metric	Observation:
- Total Requests	6,745.
- Completed Trips	2,831.
- Cancelled Trips	1,264.
- No Cars Available	2,650.
- Supply–Demand Gap	~58–60% unmet demand.

### 🕐 Time-based insights:
1. Peak demand during early morning (4–8 AM) and night (10 PM–1 AM).
2. Airport → City trips face maximum “No Cars Available”.
3. City → Airport trips face more driver cancellations.

---

## **5. Recommendations**
1. Increase driver incentives during early morning and night hours.
2. Improve Airport pickup management during high-demand periods.
3. Implement accountability for frequent driver cancellations.
4. Monitor supply-demand ratio weekly to optimize driver allocation.

---

## **6. Key Learnings**
1. How to clean and preprocess mixed-format timestamps in Excel and Python.
2. Practical SQL for analyzing real-world operational data.
3. Visual storytelling using Matplotlib and Seaborn.
4. End-to-end data analytics workflow: from raw data to insights.

---

## **7. Conclusion**
1. This project demonstrates a complete data analytics pipeline using multiple tools.
2. The analysis reveals a strong supply–demand gap in Uber’s service, particularly during early mornings and nights.
3. The findings provide actionable insights for improving driver allocation and customer satisfaction.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

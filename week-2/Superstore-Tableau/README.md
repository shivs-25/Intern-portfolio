# 📊 Advanced Sales Analysis Dashboard – Tableau

This project presents an **interactive Tableau dashboard** developed as part of the *Unit 5: Intermediate Tableau Assignment*.  
The dashboard leverages the **Sample Superstore** dataset to explore sales performance, profitability, and customer insights across regions, categories, and time periods.

---

## 🧩 Objective

To design an **interactive and analytical Tableau dashboard** that allows users to:
- Explore relationships between **Sales, Profit, and Profit Margin**
- Monitor **sales growth trends** and forecast future sales
- Identify **high-performing segments, regions, and products**
- Analyze **top and high-profit customers**
- Enable interactivity through **parameters, filters, and action-based navigation**

---

## 📂 Files Included

| File | Description |
|------|--------------|
| `Unit_5_Tableau_Assignment_Intermediate.pdf` | Assignment instructions & requirements |
| `Sample - Superstore.xls` | Source dataset for analysis |
| `Advanced_Sales_Analysis_Dashboard.twbx` | Tableau packaged workbook containing all visualizations and dashboard |
| `README.md` | This documentation file |

---

## 🗂️ Dataset Description

**Source:** Tableau’s Sample Superstore dataset (`Sample - Superstore.xls`)

**Key Fields:**
- `Order Date`, `Ship Date`, `Region`, `Category`, `Sub-Category`
- `Sales`, `Profit`, `Quantity`, `Discount`
- `Customer ID`, `Customer Name`, `Segment`
- `Product Name`, `Order ID`

**Data Cleaning:**
- Removed null entries for dates and key numeric fields
- Standardized data types (Date, Number)
- Created calculated fields for additional metrics:
  - `Profit Margin (%) = (SUM(Profit) / SUM(Sales)) * 100`
  - `Sales per Customer = SUM(Sales) / COUNTD(Customer ID)`
  - `Customer Sales (FIXED) = { FIXED [Customer ID] : SUM([Sales]) }`

---

## 📈 Visualizations Created

### 1. Sales vs Profit Scatter Plot
- **Purpose:** Examine correlation between sales volume and profit.
- **Features:**  
  - Color: Profit Margin (%)  
  - Size: Sales volume  
  - Trend line: Linear regression added for relationship visualization  
  - Tooltip: Displays product, category, sales, and profit margin  

---

### 2. Customer Segment Analysis (Parameter-driven)
- **Purpose:** Compare average performance across customer segments.
- **Features:**  
  - Parameter: `Metric Selector` (Sales / Profit)  
  - Dynamic title updates with selected metric  
  - Bars sorted descending for clarity  
  - Tooltip with sales, profit, and margin info  

---

### 3. Sales Growth Over Time (with Forecast)
- **Purpose:** Track monthly/quarterly/yearly trends and project future sales.
- **Features:**  
  - Parameter: `Time Granularity` (Month / Quarter / Year)  
  - Reference line for average monthly sales  
  - 6-month forecast enabled using Tableau’s forecasting model  
  - Clean, annotated trend line with tooltips  

---

### 4. Regional Profit Heatmap
- **Purpose:** Identify profit distribution across regions and categories.
- **Features:**  
  - Rows: Region | Columns: Category  
  - Color: Profit intensity (green = high, red = loss)  
  - Filter: Sub-Category and Region filters enabled globally  
  - Tooltip: Sales, Profit, Margin, Order Count  

---

### 5. Top 5 Products Dashboard (Bar + Line Combo)
- **Purpose:** Highlight the top 5 products by sales with profit overlay.
- **Features:**  
  - Dual-axis: Bars (Sales) and Line (Profit)  
  - INDEX() table calculation to dynamically select Top 5  
  - Interactive **action filter** – click on a category to filter top products  
  - Tooltips and color legends for enhanced readability  

---

## ⚙️ Advanced Tableau Features Used

| Feature | Description |
|----------|--------------|
| **Calculated Fields** | Profit Margin, Sales per Customer, Customer Sales (LOD) |
| **Parameters** | Metric Selector, Time Granularity |
| **Forecasting** | 6-month prediction using Tableau’s exponential smoothing model |
| **LOD Expressions** | Fixed calculations for Customer-level aggregations |
| **Sets & Filters** | Top 10% by Sales, Top 20% by Profit customers |
| **Action Filters** | Clicking a region/category updates dependent charts |
| **Dynamic Titles** | Parameter-driven text titles |
| **Annotations** | Highlighting key trends and outliers |
| **Dashboard Design** | Interactive layout with consistent color and formatting |

---

## 🔍 Insights Summary

- **Profitability varies by product**: Certain high-sales products generate low or negative profit margins.
- **Regional differences**: Western and Central regions lead in sales, but profitability is strongest in the South.
- **Customer segmentation**: Corporate and Consumer segments contribute most revenue, but the Home Office segment is less profitable.
- **Time trend**: Sales growth follows a steady upward trajectory with visible seasonal spikes; 6-month forecast predicts continued growth.
- **Customer concentration**: Top 10% of customers contribute over 40% of total sales; top 20% by profit are prime for retention efforts.

---

## 🧭 How to Use the Dashboard

1. Open `Advanced_Sales_Analysis_Dashboard.twbx` in Tableau Desktop or Tableau Public.
2. Use the **Metric Selector parameter** to toggle between Sales and Profit views.
3. Adjust **Time Granularity** (Month / Quarter / Year) in the Sales Growth chart.
4. Click any **Category or Region** to filter related visualizations dynamically.
5. Hover over points, bars, and heatmap squares for detailed tooltips.

---

## 🧠 Key Learnings

- Using **parameters** to drive dynamic measures and titles.
- Building **LOD calculations** for stable customer-level aggregation.
- Combining **forecasting and trend analysis** for actionable insights.
- Applying **dual-axis charts** for comparative visualization.
- Designing **intuitive interactive dashboards** with action filters.

---

## 💻 Tools Used

- **Tableau Desktop / Tableau Public**
- **Microsoft Excel** (for dataset)
- **GitHub** (for version control and documentation)
- **Markdown** (for README documentation)

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

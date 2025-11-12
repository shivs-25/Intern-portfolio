# ⚡ Electric Vehicle (EV) Dashboard – India (2021–2024)

## 📖 Overview
This project presents an **interactive Power BI dashboard** analyzing the growth of electric vehicle (EV) adoption in India between **2021 and 2024**.  
It visualizes state-wise sales, manufacturer performance, seasonal trends, cost comparisons, and government incentives, providing a complete picture of India’s EV ecosystem.

The dashboard was developed as part of an academic data visualization project and is designed to support data-driven decision-making for policymakers, manufacturers, and investors.

---

## 🧩 Key Features
- 📊 **State-Wise EV Sales & Penetration**  
  Combination chart showing total EV sales vs. EV share of total vehicle sales across Indian states.

- 🏭 **Top 5 EV Manufacturers (2W & 4W)**  
  Identifies the leading manufacturers by sales volume.

- 📈 **CAGR (Growth %) by State and Manufacturer**  
  Highlights the fastest-growing regions and brands in EV adoption.

- 📆 **Seasonal EV Sales Trends**  
  Multi-line chart showing monthly sales patterns and yearly growth cycles.

- 💰 **Cost Comparison: EV vs Petrol vs Diesel**  
  Demonstrates annual and per-km running cost differences between vehicle types.

- 🗺️ **Government Incentives Map**  
  Geographic visualization showing state-wise EV subsidies and policy support.

---

## 📂 Dataset Details
The dashboard is built using the following datasets:

| File Name | Description |
|------------|-------------|
| `electric_vehicle_sales_by_state.csv` | EV and total vehicle sales by Indian state |
| `electric_vehicle_sales_by_makers.csv` | Manufacturer-wise EV sales and categories |
| `dim_date.csv` | Date dimension table (used for fiscal periods and time analysis) |
| `cost_comparison.csv` | Annual and per km running cost of EVs, Petrol, Diesel vehicles |
| `ev_incentives.csv` | State-wise EV subsidy and incentive data |

> 🧠 All data files are cleaned and structured to integrate via Power BI’s data model. Relationships are based on the `date` and `state` fields.

---

## 🛠️ Tools & Environment
- **Tool Used:** Power BI (Desktop & Service)  
- **Platform:** Power BI Web (Mac) / Power BI Desktop (Windows)  
- **File Format:** `.pbix`, `.csv`, `.pdf`  
- **Language:** DAX (for calculated measures like CAGR & Penetration Rate)

---

## ⚙️ Measures and Calculations
1. Some of the key DAX calculations used:
   ```DAX
   Penetration Rate =
   DIVIDE(
    SUM('electric_vehicle_sales_by_state'[Electric_Vehicles_Sold]),
    SUM('electric_vehicle_sales_by_state'[Total_Vehicles_Sold])
   )

   CAGR =
   VAR StartYear = CALCULATE(SUM('electric_vehicle_sales_by_state'[Electric_Vehicles_Sold]), FILTER('dim_date', 'dim_date'[fiscal_year] = 2021))
   VAR EndYear   = CALCULATE(SUM('electric_vehicle_sales_by_state'[Electric_Vehicles_Sold]), FILTER('dim_date', 'dim_date'[fiscal_year] = 2024))
   VAR Years     = 3
   RETURN
   ((EndYear / StartYear) ^ (1 / Years)) - 1

---

## 💡 Insights Derived
1. Fastest-Growing State: Meghalaya – CAGR 476% (rapid growth from low base).
2. Top Markets: Maharashtra, Karnataka, and Delhi lead total EV sales.
3. Leading Manufacturers: Ola Electric, Ather, TVS (2W); Tata Motors, Mahindra (4W).
4. Peak Sales Months: March & November (financial year-end & festive season).
5. Cost Savings: EVs cost only ₹29K/year to operate, vs ₹1.1–1.2L for fossil-fuel vehicles.
6. Best Incentives: Maharashtra offers up to ₹1L subsidy per vehicle.

---

## 📈 Results & Learning Outcomes
1. Learned data modeling and DAX formula creation in Power BI.
2. Designed interactive, multi-visual dashboards using real-world EV datasets.
3. Understood cost competitiveness and policy impact on EV adoption.
4. Built a polished, submission-ready report suitable for professional portfolios.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

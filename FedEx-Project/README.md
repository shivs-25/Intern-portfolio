# Exploratory Data Analysis on FedEx Delivery Operations

- This project performs a **comprehensive exploratory data analysis (EDA)** on FedEx delivery operations to uncover key insights about delivery times, shipping costs, operational delays, and customer segments.
- It is designed to highlight practical data-cleaning, visualization, and business analysis skills using Python.

---

## 📘 Project Overview

The primary goal of this project is to analyze FedEx delivery patterns and operational performance using a structured EDA workflow.  
This project demonstrates how data-driven insights can optimize logistics, improve service reliability, and reduce costs.

### **Key Objectives**
1. **Understand and clean** the dataset (missing values, datatypes, derived columns).  
2. **Explore** univariate and bivariate distributions.  
3. **Investigate operational patterns** across shipment modes, delay reasons, and customer segments.  
4. **Derive actionable business insights** and recommendations.

---

## 🧾 Dataset Description

The dataset (`fedex_deliveries.csv`) is a **simulated but realistic** FedEx operational dataset containing 5,000 shipment records.  
Each record captures shipment-level details such as origin, destination, shipment mode, cost, and delays.

| Column Name        | Description |
|--------------------|-------------|
| `ShipmentID`       | Unique shipment identifier |
| `Origin`           | Origin city of the shipment |
| `Destination`      | Destination city of the shipment |
| `Pickup_Date`      | Date the shipment was picked up |
| `Delivery_Date`    | Date the shipment was delivered |
| `Delivery_Status`  | Delivery status (Delivered, Delayed, In Transit) |
| `Distance_KM`      | Distance between origin and destination (km) |
| `Shipment_Mode`    | Transport mode (Air, Ground, Freight) |
| `Weight_KG`        | Shipment weight (kg) |
| `Cost_USD`         | Shipping cost (USD) |
| `Customer_Segment` | Type of customer (Business, Retail, Government) |
| `Delay_Reason`     | Cause of delay (Weather, Operational, Customs, None) |

> 🧩 Note: The dataset is synthetically generated for educational purposes and does not represent actual FedEx data.

---

## 🧠 Analysis Workflow

### 1. **Data Cleaning & Preparation**
- Handle missing values (median/mode imputation)
- Parse date columns and calculate `Delivery_Time_Days`
- Ensure numeric consistency and fix datatypes

### 2. **Exploratory Data Analysis (EDA)**
- **Univariate Analysis:** Distribution of delivery times, costs, weights  
- **Bivariate Analysis:** Relationships between shipment mode, cost, and delivery status  
- **Operational Insights:** Delay reasons, top city pairs, customer segment trends  
- **Correlation Analysis:** Cost, distance, weight, and delivery time

### 3. **Business Insights**
- Identify operational inefficiencies and cost-drivers  
- Recommend mode optimization and proactive customer communication strategies  
- Highlight performance improvement opportunities across segments

---

## 📊 Visualizations

Some of the key visuals generated in the notebook include:

- Delivery Time Distribution Histogram  
- Shipment Volume by Mode  
- Average Cost per Customer Segment  
- Delivery Status Composition (stacked bar)  
- Weight vs. Cost Scatter Plot  
- Correlation Heatmap  
- Average Delivery Time by Delay Reason and Mode

Each visualization includes proper titles, axis labels, and interpretations.

---

## 🧰 Tools & Libraries

| Tool / Library | Purpose |
|----------------|----------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computation |
| `matplotlib` | Data visualization |
| `Jupyter Notebook` | Interactive analysis environment |

---

## 🚀 How to Run This Project

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/FedEx-EDA.git
   cd FedEx-EDA
2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib
3. **Run the notebook**
   ```bash
   jupyter notebook FedEx_Delivery_EDA.ipynb

---

## 💡 Key Insights
1. Average Delivery Time: Typically ranges between 1–4 days depending on mode and distance.
2. Shipment Mode: Ground dominates shipment count; Air is fastest but costliest.
3. Customer Segments: Business customers form the largest share, with more predictable cost patterns.
4. Delay Reasons: Weather and Customs delays lead to significantly higher delivery times.
5. Operational Focus: Improving customs processes and mode selection can yield efficiency gains.

---

## 🏁 Conclusion
### This project demonstrates:
- Strong data cleaning and EDA workflow skills.
- Clear visual storytelling for business decision-making.
- Ability to translate operational data into insights.
### 📈 This analysis highlights how data science can transform logistics into a more efficient and customer-centric operation.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

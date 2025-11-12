# 🏙️ Dubai Real Estate Intelligence Dashboard

A complete **data analytics and visualization project** built in **Power BI**, designed to analyze the Dubai housing market and provide data-driven insights for buyers, investors, and developers.

---

## 📘 Project Overview

This project explores **Dubai's residential real estate** market using a structured dataset of property listings.  
The dashboard delivers key insights into pricing trends, property sizes, area types, and market segmentation by price category.

It forms part of my **Data Analytics portfolio** and was created as part of an academic assignment to demonstrate:
- Data cleaning and transformation
- Creation of calculated columns and measures
- Dashboard design and storytelling using Power BI

---

## 🧩 Dataset Details

**Source:** Provided by the course instructor  
**File:** `housing_price_dataset.csv` → cleaned and enhanced to `dubai_housing_enriched.csv`

**Final columns used:**
| Column | Description |
|--------|-------------|
| `location` | Area type (Urban / Suburb / Rural) |
| `price` | Property price in AED |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `size_sqft` | Property size in square feet |
| `year_built` | Construction year |
| `price_per_sqft` | Calculated as `price / size_sqft` |
| `property_age` | Calculated as `2025 - year_built` |
| `listing_category` | Segmentation into Budget / Mid-Range / High-End |
| `listing_category_order` | Numeric sort order (1, 2, 3) |

---

## 🧹 Data Cleaning & Preparation

All data cleaning and preprocessing were completed in Power BI (Power Query) and Python.  
Key steps included:
1. Removing duplicates and handling missing values  
2. Converting column data types (numeric / text)  
3. Replacing invalid entries (e.g., `size_sqft <= 0` → null)  
4. Creating calculated columns:
   - `price_per_sqft`
   - `property_age`
   - `listing_category` (based on price quantiles)
   - `listing_category_order`
5. Sorting listing categories correctly  
6. Formatting numbers and currency (AED)

---

## 📊 Power BI Dashboard Overview

The **Dubai Housing Dashboard** provides a one-page summary of the market, with interactive slicers and visuals.

### 🔹 Key KPIs
| Metric | Description |
|--------|-------------|
| **Total Listings** | 50K total properties |
| **Average Price (AED)** | 224.93K |
| **Average Size (sqft)** | 2.01K |
| **Highest Priced Property (AED)** | 492K |
| **Average Price per Sqft (AED)** | 113.4 |
| **Average Property Age** | 39.6 years |

### 🔹 Core Visuals
- **KPI Cards:** Total Listings, Avg Price, Avg Size, Highest Price, Avg Price/Sqft  
- **Bar Chart:** Average Price by Area Type (Urban/Rural/Suburb)  
- **Column Chart:** Bedrooms by Price Category  
- **Treemap:** Listings by Listing Category (Budget/Mid/High-End)  
- **Bar Chart:** Avg Price per Sqft by Area Type  
- **Slicers:** Location, Bedrooms, Price (Between), Listing Category  
- *(Optional)* Textbox with insights and recommendations

---

## 💡 Insights & Recommendations

- **Urban properties** are priced slightly higher (AED 227K) than rural and suburban areas.  
- **Price per sqft** remains consistent (~AED 113–114), showing stable demand.  
- **2–3 bedroom** properties dominate listings, particularly in mid-range categories.  
- **Suburban listings** offer similar PPSF but lower total price → strong **value-for-money**.  
- **High-end properties** are concentrated in 4+ bedroom listings → ideal for investors.  
- Developers should focus on **mid-range inventory** in **urban/suburban** areas.

---

## 🧠 Tools & Technologies Used

| Category | Tools |
|-----------|-------|
| **Data Cleaning** | Power Query, Python (pandas, numpy) |
| **Data Visualization** | Power BI Desktop |
| **Modeling** | DAX Measures, Calculated Columns |
| **File Formats** | `.csv`, `.pbix`, `.pptx`, `.ipynb` |
| **Language** | DAX, Python |

---

## DAX Measures
1. Used formulae:
   ```DAX
   Total Listings = COUNTROWS('dubai_housing_enriched')
   Average Price = AVERAGE('dubai_housing_enriched'[price])
   Average Size (sqft) = AVERAGE('dubai_housing_enriched'[size_sqft])
   Avg Price per Sqft = AVERAGE('dubai_housing_enriched'[price_per_sqft])
   Highest Priced Property = MAX('dubai_housing_enriched'[price])
   Listing Count = COUNT('dubai_housing_enriched'[price])

---

## 📈 Learning Outcomes
1. End-to-end data analytics workflow (from raw data → insights).
2. Creating calculated columns and measures in Power BI.
3. Designing KPI-driven dashboards.
4. Storytelling through visuals and actionable insights.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

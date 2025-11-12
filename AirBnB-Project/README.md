# Airbnb Data Analysis and Interactive Dashboard

## 📊 Project Overview
1. This project explores Airbnb listings data for New York City to uncover insights into pricing, room types, neighbourhood trends, and availability patterns.
2. It includes both a Jupyter Notebook (EDA + insights) and an interactive Streamlit dashboard for visual exploration.

---

## 🎯 Objectives
- Clean and preprocess Airbnb data (listings.csv).
- Perform exploratory data analysis (EDA) and visualize trends.
- Build an interactive Streamlit dashboard to explore listings.
- Provide business insights and actionable recommendations.

---

## 🧩 Dataset
- All data is sourced from the Inside Airbnb public repository.
- For reproducibility, the Streamlit app and notebook automatically download the latest listings.csv.

---

## 🧹 Data Cleaning Steps
1. Removed duplicates and standardized column names.
2. Cleaned price values by stripping $ and commas, converting to numeric.
3. Filled missing numeric values with median, categorical with "Unknown".
4. Parsed date columns where applicable.
5. Exported a cleaned version (cleaned_listings.csv) for dashboard and report use.

---

## 📊 Exploratory Data Analysis (EDA)
1. Key visualizations in the notebook and dashboard include:
   - Price Distribution (filtered for outliers).
   - Listings by Neighbourhood.
   - Price by Room Type (Box Plot).
   - Price vs. Number of Reviews (Scatter).
   - Correlation Heatmap (Numerical Features).
2. Additional analyses:
   - Linear Regression (optional) for predicting prices.
   - K-Means Clustering (optional) to identify market segments.

---

## 🧠 Key Insights
1. The majority of NYC Airbnb listings are priced below $300/night.
2. “Entire home/apt” listings are the most common and most expensive type.
3. Manhattan dominates the listings count and average price.
4. Price and number of reviews show a mild negative relationship (higher-priced listings tend to have fewer reviews).
5. Numeric features show moderate correlations between availability and price.

---

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/airbnb-nyc-dashboard.git
   cd airbnb-nyc-dashboard
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. (Optional) Download the dataset manually:
   ```bash
   python fetch_nyc_data.py
6. Launch the Streamlit dashboard:
   ```bash
   streamlit run app.py
Open the link Streamlit provides (usually http://localhost:8501).

---

## 💡 Future Improvements
1. Add sentiment analysis using reviews.csv text data.
2. Include seasonality trends using calendar.csv.
3. Deploy Streamlit app on Streamlit Community Cloud or Render.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

# Zomato Restaurant Reviews – Exploratory Data Analysis (EDA)

This project performs an **end-to-end exploratory data analysis (EDA)** on Zomato restaurant reviews and metadata.  
It involves **data cleaning, preprocessing, merging, and visual exploration** to extract insights about restaurant ratings, cuisines, and overall trends.

---

## 📊 Project Overview

The dataset includes:
- **Restaurant reviews:** Ratings, text reviews, timestamps, and user info.
- **Restaurant metadata:** Name, cuisine types, cost, collection tags, and timings.

We explore:
1. How ratings are distributed across restaurants.
2. Which cuisines are most popular.
3. Which restaurants have the highest average ratings (based on sufficient reviews).
4. The correlation between numeric variables.

---

## 🧠 Key Insights

- Average rating across all reviews is around **3.6**.
- Ratings are moderately concentrated between **3.0 – 4.5**.
- Top-rated restaurants consistently maintain ratings **above 4.2**.
- Most frequent cuisines include **North Indian**, **Chinese**, and **Fast Food**.
- Numeric fields show **weak correlations** with ratings — suggesting qualitative factors matter more (e.g., food quality, service, ambiance).

---

## 🧹 Data Cleaning Steps

1. Standardized column names and trimmed whitespace.  
2. Converted rating values to numeric and parsed review timestamps.  
3. Removed duplicates and missing values.  
4. Normalized restaurant names (casefold + whitespace cleanup).  
5. Merged review data with metadata using a normalized key.

---

## 🧩 File Descriptions

| File | Description |
|------|--------------|
| `Zomato_EDA_Final.ipynb` | Main notebook — includes code, plots, and insights |
| `data/` | Contains raw datasets (CSV files) |
| `outputs/clean_reviews.csv` | Cleaned reviews data |
| `outputs/clean_metadata.csv` | Cleaned metadata |
| `outputs/merged_zomato.csv` | Final merged dataset |
| `outputs/plots/` | Saved visualization charts |
| `requirements.txt` | Python dependencies list |

---

## 📈 Visuals

| Visualization | Description |
|----------------|--------------|
| **Rating Distribution** | Histogram showing how user ratings are spread |
| **Top Restaurants** | Bar chart of restaurants with highest average ratings |
| **Top Cuisines** | Most common cuisine types |
| **Correlation Matrix** | Numeric feature relationships |

---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/zomato-eda-project.git
   cd zomato-eda-project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the notebook:
   ```bash
   jupyter notebook Zomato_EDA_Final.ipynb

---

## 🧾 Summary 
1. The analysis reveals that Zomato’s customer base generally provides positive ratings, with most restaurants scoring between 3 and 4.5.
2. High-rated restaurants tend to have both strong engagement and consistent service quality.
3. North Indian and Chinese cuisines dominate across cities, showing their mass appeal.
4. There is no strong numerical correlation between cost and rating, highlighting the importance of subjective experience in customer satisfaction.
5. Overall, the Zomato dataset shows healthy user activity, predictable rating patterns, and clear opportunities for promoting high-performing establishments.

---

## 🧠 Key Insights from the Zomato Restaurant Reviews EDA

1. Rating Overview
   - The average rating across all restaurants is around 3.6 (on a 5-point scale).
   - Most ratings cluster between 3.0 and 4.5, showing a generally positive customer sentiment.
   - The rating distribution is right-skewed — meaning most customers give good ratings, while very low scores are rare.

2. Top Restaurants
   -Restaurants with more than 20 reviews and average ratings above 4.2 stand out as consistent top performers.
   These venues tend to appear repeatedly in popular Zomato collections (like “Best of City” or “Trending Now”).
   The combination of high review count and high average rating indicates genuine popularity rather than a few isolated high scores.

3. Cuisine Insights
   The most common cuisines (by frequency across restaurants) are typically:
   - North Indian
   - Chinese
   - Fast Food
   These dominate the Zomato listings, reflecting India’s mainstream urban dining preferences.
   Secondary cuisines (like Italian, Continental, and Mughlai) are present but in smaller proportions.

4. Cost and Value Patterns
   - Moderate-cost restaurants tend to receive the widest spread of ratings — suggesting that mid-range pricing sees both highly satisfied and disappointed customers.
   - Extremely cheap or expensive places have more consistent ratings, possibly because expectations are clearer at those extremes.
  
5. Correlation Findings
   - There is no strong correlation between numerical fields (like cost or rating) — suggesting that qualitative factors (service quality, ambiance, delivery speed, etc.) drive customer ratings more than price.
   - This insight aligns with typical restaurant review behavior — satisfaction is subjective, not strictly price-dependent.

6. Data Quality & Cleaning Notes
   - Around 3–5% of ratings were missing and were replaced with the mean rating (≈3.6).
   - Minor text normalization was required on restaurant names (case, spacing).
   - No significant duplicate records remained after cleaning.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

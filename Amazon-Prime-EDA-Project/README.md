# Amazon Prime Video EDA Project

## 📊 Project Overview
This project performs an **Exploratory Data Analysis (EDA)** on the *Amazon Prime Video Movies & TV Shows* dataset to uncover trends, patterns, and insights about the content available on the platform.  

The analysis includes data cleaning, feature engineering, and visualization of key metrics such as genre distribution, age certifications, release year trends, popular countries, and content duration.

---

## 🧰 Tech Stack & Tools
- **Language:** Python (3.10+)
- **Libraries:**
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn *(optional, for ML section)*
- **Environment:** Jupyter Notebook / Google Colab
- **Dataset:** Amazon Prime Video Titles (titles.csv, credits.csv)

---

## 🗂️ Dataset Description
The dataset contains details about movies and TV shows available on Amazon Prime Video, including:
- `title` — Title of the content  
- `type` — Movie or TV Show  
- `release_year` — Year of release  
- `age_certification` — Age rating (G, PG-13, R, etc.)  
- `runtime` — Duration in minutes or number of seasons  
- `genres` — Comma-separated list of genres  
- `production_countries` — Origin countries  
- `imdb_score`, `tmdb_score`, `popularity`, etc.

Additional information (e.g. directors, cast) is available in `credits.csv`.

---

## 🧹 Data Cleaning & Preparation
Key steps:
1. **Handled missing values** in categorical and numeric columns.
2. **Removed duplicates** using cleaned title and release year.
3. **Created helper columns:**
   - `title_clean` — normalized title text
   - `type_clean` — standardized content type (“Movie”, “TV Show”)
   - `duration_raw` — parsed from `runtime`
   - `genre_list` — exploded from comma-separated genres
   - `country_list` — parsed from `production_countries`
4. **Converted release_year** to numeric for analysis.
5. **Saved cleaned dataset** to `cleaned_titles.csv`.

---

## 📈 Exploratory Data Analysis
The EDA explores:
- 🔹 **Content type distribution** (Movies vs. TV Shows)
- 🔹 **Top genres and genre trends**
- 🔹 **Age certification breakdown**
- 🔹 **Release year trends**
- 🔹 **Country of production analysis**
- 🔹 **Duration patterns** (runtime in minutes, number of seasons)
- 🔹 **Correlation between IMDb / TMDb scores**

Each visualization is saved as a PNG file in the `/plots` folder.

---

## 💡 Key Insights
- Amazon Prime has a **larger movie catalog** compared to TV shows.  
- Most content is rated **13+ or 16+**, indicating a focus on young adult audiences.  
- **Drama, Comedy, and Action** are the most common genres across both movies and shows.  
- A significant increase in original content production occurred **after 2015**.  
- The **U.S.** dominates content production, but international titles have grown steadily.  

---

## 💬 Recommendations
1. **Expand localization** — Increase non-English titles to capture global audiences.  
2. **Leverage popular genres** — Focus marketing and production on high-performing genres (Drama, Action, Thriller).  
3. **Target family-friendly content** — Increase PG / G-rated titles to balance current age-rating skew.

---

## 🤖 Optional Machine Learning
An optional Logistic Regression model was included to classify whether a title is a **Movie or TV Show** based on features like runtime, number of genres, and release year.

1. To enable ML:
   ```bash
   pip install scikit-learn

---

## 🏁 Results
1. Fully cleaned dataset (cleaned_titles.csv).
2. Comprehensive EDA with clear visualizations.
3. Actionable insights & business recommendations.
4. Optional ML classifier (for bonus analytics).

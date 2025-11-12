# Tennis Analytics: Unlocking Tennis Data with SportRadar API

This project explores professional tennis data using the SportRadar API.  
It demonstrates a complete data analytics workflow — from data extraction and database design to SQL querying, visualization, and interactive dashboarding.

---

## 🎯 Project Overview

This project is part of a **Game Analytics** assignment focusing on unlocking insights from tennis data.  
It covers the entire data pipeline:

1. **Data Extraction** – Using SportRadar API (Trial key) to fetch tennis competitions, categories, and season data.
2. **Data Cleaning & Transformation** – Processed using Python and Pandas.
3. **Database Design** – Normalized SQLite database with relationships between competitions, categories, seasons, and player rankings.
4. **SQL Analysis** – Efficient analytical queries for insights.
5. **Visualization** – Inline plots using `matplotlib` and `seaborn`.
6. **Streamlit Dashboard** – Interactive UI for exploring trends, countries, and player performance.

---

## 🧱 Project Architecture

| Layer | Technology | Description |
|--------|-------------|-------------|
| Data Source | SportRadar Tennis API | Primary data source |
| Extraction | Python (`requests`) | API integration and CSV generation |
| Storage | SQLite | Normalized relational database |
| Analysis | SQL + Pandas | Querying and processing data |
| Visualization | Matplotlib, Seaborn | Exploratory data visuals |
| App | Streamlit | Interactive dashboard with filters |

---

## 📊 Key Insights

- **Top Players**: Highlights top-ranked players and their performance points.  
- **Country Analysis**: Shows which countries dominate tennis rankings.  
- **Seasonal Growth**: Trends in competition frequency by year.  
- **Player Consistency**: Identifies players with steady or volatile performance.  

---

## ⚙️ How to Run

1. Clone the Repository
   ```bash
   git clone https://github.com/<your-username>/Tennis-Analytics.git
   cd Tennis-Analytics

2. Install Requirements
   ```bash
   pip install -r requirements.txt

3. Run the Jupyter Notebook
   ```bash
   jupyter notebook tennis_analysis.ipynb

4. Launch the Streamlit App
   ```bash
   streamlit run app.py

5. The dashboard will open in your browser at
   ```bash
   http://localhost:8501

---

## 🧠 Features
1. Automated API data fetching and CSV saving.
2. End-to-end ETL pipeline with SQLite.
3. Interactive analytics dashboard.
4. Query optimization and schema normalization.
5. Clear visual storytelling with contextual insights.

---

## 🧠 Future Improvements
1. Live API refresh scheduling.
2. Player performance prediction using machine learning.
3. Integration with tournament-level event statistics.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

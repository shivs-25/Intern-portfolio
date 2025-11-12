# 📊 Stock Market Analysis using SQL

> A complete data analysis project using **SQL and Python** to explore, clean, and analyze stock price data for six major Indian companies.  
> This project demonstrates end-to-end data handling — from preprocessing to insights — with both SQL queries and Python visualizations.

---

## 🧭 Overview

This project analyzes the historical stock data of **Bajaj Auto**, **Eicher Motors**, **Hero Motocorp**, **Infosys**, **TCS**, and **TVS Motors**.  
Using SQL, we calculate long-term trends, detect buy/sell signals, identify trading opportunities, and rank company performance.

The project demonstrates how SQL can be leveraged for real-world **financial time-series analysis**, backed by Python for automation and visualization.

---

## ⚙️ Technologies Used

| Tool / Language | Purpose |
|-----------------|----------|
| **Python (Pandas, SQLite3, Matplotlib)** | Data preprocessing, database creation, and visualization |
| **SQL (SQLite)** | Querying trends, calculating performance metrics, generating signals |
| **Jupyter Notebook** | Integrated code + documentation environment |
| **ReportLab** | Automated PDF report generation |
| **MS PowerPoint** | Presentation summarizing project outcomes |

---

## 📂 Dataset Description

Each dataset represents one company’s historical daily stock data.  
**Common attributes include:**

| Column | Description |
|--------|-------------|
| `Date` | Trading date |
| `Open` | Opening price of the day |
| `High` | Highest traded price |
| `Low`  | Lowest traded price |
| `Close` | Closing price of the day |
| `Volume` | Number of shares traded |

---

## 🧩 Key SQL Tasks Performed

1. **Trend Analysis** — Calculate total percentage change for each company.  
2. **Fixed-Window Trend (2015–2018)** — Measure mid-term performance.  
3. **Buy/Sell Signal Generation** — Identify 3-day momentum-based buy/sell points.  
4. **Latest Recommendation** — Combine momentum signals with overall growth.  
5. **Min/Max Closing Prices** — Identify volatility and range.  
6. **Opportunities Detection** — Estimate total buy/sell pairs and profit from 1 share.  
7. **Performance Ranking** — Rank all companies by overall growth.

---

## 📈 Visualizations

| Visualization | Description |
|---------------|--------------|
| **Line Chart** | Closing Price Trends Over Time (per company) |
| **Bar Chart** | Percentage Growth Comparison |
| **Signal Plot** | BUY/SELL markers overlayed on price chart |
| **Bar Chart** | Trading Opportunities per Company |
| **Bar Chart** | Estimated Profit (1 Share) per Company |

All visualizations were created using **Matplotlib** for simplicity.

---

## 🔍 Insights & Observations

- **TCS** and **Infosys** were the **top-performing stocks** in terms of overall growth.  
- **Bajaj Auto** and **Hero Motocorp** showed **frequent trading opportunities** (ideal for active traders).  
- **Eicher Motors** displayed **high volatility**, suitable for risk-tolerant investors.  
- Momentum-based signals proved effective for capturing trend reversals.  
- SQL enabled **clean, repeatable financial analytics** directly on structured data.

---

## 💡 Recommendations

- **Long-Term Investors:** Focus on TCS and Infosys for steady returns.  
- **Short-Term Traders:** Explore Bajaj Auto and Hero Motocorp for active trading.  
- **High-Risk Traders:** Eicher Motors offers high upside potential but high risk.  

---

## 🧠 Learning Outcomes

- Efficient use of **SQL window functions** for time-series analysis  
- Integration of **SQL + Python** for hybrid analytical workflows  
- Understanding of **momentum-based trading logic**  
- Automation of data cleaning and visualization pipelines

---

## 🚀 How to Run This Project

### Prerequisites
Ensure you have:
- Python 3.8+  
- Jupyter Notebook  
- Libraries: `pandas`, `sqlite3`, `matplotlib`, `reportlab`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/SQL-Stock-Market-Analysis.git
   cd SQL-Stock-Market-Analysis

2. Open the Jupyter notebook
   ```bash
   jupyter notebook SQL_Stock_Market_Analysis_Detailed.ipynb

3. Run all cells
The notebook will generate the SQLite DB, reports, and visualizations.

---

## 📌 Future Enhancements
1. Add technical indicators (SMA, EMA, RSI, Bollinger Bands).
2. Build a web dashboard for live tracking.
3. Integrate APIs for real-time market data.
4. Use Machine Learning for predictive stock forecasting.

---

## Author

**Shivali Muthukumar | Data Analyst**

---

## 🪪 License

This project is released under the **MIT License**.  
Feel free to reuse the code, calculations, or design ideas with proper credit.

---

### ⭐ If you found this dashboard insightful, please star this repository on GitHub!

# Capstone Project: Housing Price Prediction with EDA & Machine Learning  

## 📘 Overview
This project combines **Exploratory Data Analysis (EDA)** and **Machine Learning** to predict housing prices using the **Ames Housing Dataset**. The workflow includes data exploration, model training, and deployment through a simple **web interface** for real-time predictions.  

---

## 🎯 Objectives  
- Perform comprehensive **EDA** to understand housing market trends.  
- Engineer features and build a **regression model** to predict prices.  
- Integrate the model into a **Flask-based web app** for user interaction.  
- Present the results using a **presentation deck** and **video explanation**.  

---

## 🧠 Methodology  

### 1. **Exploratory Data Analysis (EDA)**  
Performed using `EDA Analysis.py`:
- Data cleaning (handling missing values, formatting numeric types).  
- Visual exploration of features (e.g., correlations, distributions).  
- Identification of top predictive features like `OverallQual`, `GrLivArea`, and `GarageCars`.  

### 2. **Model Development**  
Implemented in `housing_predictor.py`:
- Used **Linear Regression** / **Random Forest Regressor** for price prediction.  
- Split data into training and testing sets using `train_test_split`.  
- Evaluated using **R²**, **MAE**, and **RMSE** metrics.  
- Saved the model using `pickle` for deployment.  

### 3. **Web App Interface**  
`index.html` provides a simple, user-friendly interface:
- Users input home features (e.g., lot area, garage size, year built).  
- The Flask backend predicts and displays the **estimated home price** dynamically.  

---

## ⚙️ Technologies & Libraries
1. Python 3.10+.
2. Flask – for the web app interface.
3. Pandas, NumPy – data processing.
4. Scikit-learn – model training and evaluation.
5. Matplotlib, Seaborn – visualizations.
6. HTML/CSS – frontend design.

---

## 🚀 How to Run the Project
### 1. Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd week-2

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the Flask app
python housing_predictor.py

### Then open your browser and go to:
➡️ http://127.0.0.1:5000/

---

## 📊 Key Insights
1. Overall Quality and GrLivArea are the most influential features.
2. Houses with larger garages and recent renovations tend to have higher prices.
3. The model achieves an R² score of ~0.88, showing good predictive performance.

---

## 🏁 Conclusion
1. This capstone demonstrates a full data science pipeline — from raw data to deployment.
2. It showcases analytical reasoning, model-building expertise, and basic web development skills essential for real-world machine learning applications.

---

# Author: Shivali Muthukumar | Data Analyst

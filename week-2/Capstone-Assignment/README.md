# Capstone Project: Housing Price Prediction with EDA & Machine Learning  

## 📘 Overview
This project combines **Exploratory Data Analysis (EDA)** and **Machine Learning** to predict housing prices using the **Ames Housing Dataset**.  
The workflow includes data exploration, model training, and deployment through a simple **Flask-based web interface** for real-time predictions.  

---

## 🎯 Objectives  
- Perform comprehensive **EDA** to understand housing market trends.  
- Engineer features and build a **regression model** to predict prices.  
- Integrate the model into a **Flask web app** with a user-friendly interface.  
- Present the results using a **presentation deck** and **video explanation**.  

---

## 🧠 Methodology  

### 1. **Exploratory Data Analysis (EDA)**  
Performed using `EDA Analysis.py`:
- Cleaned and prepared the dataset (handled missing values, formatted numeric types).  
- Conducted visual analysis to identify feature distributions and correlations.  
- Highlighted key predictive features such as `OverallQual`, `GrLivArea`, and `GarageCars`.  

### 2. **Model Development**  
Implemented in `housing_predictor.py`:
- Built and trained **Linear Regression** and/or **Random Forest** models for price prediction.  
- Used `train_test_split` for model validation.  
- Evaluated performance using **R²**, **MAE**, and **RMSE** metrics.  
- Saved the trained model with `pickle` for deployment in the web app.  

### 3. **User Interface & Web App**  
Implemented using both `User Interface Prediction.py` and `index.html`:  
- `User Interface Prediction.py` handles user input and connects the trained model with the web interface.  
- `index.html` provides a clean form where users can enter housing details.  
- Flask renders the prediction dynamically and displays the estimated price on the webpage.  

---

## ⚙️ Technologies & Libraries
1. Python 3.10+.
2. Flask – for the web app interface.
3. Pandas, NumPy – data processing.
4. Scikit-learn – model training and evaluation.
5. Matplotlib, Seaborn – visualizations.
6. HTML/CSS – frontend design.

---

## 🗃️ File Setup & Organization
### To ensure all files work properly, follow these steps when saving your project locally or uploading to GitHub:

week-2/
├── AmesHousing.csv
├── EDA Analysis.py
├── housing_predictor.py
├── User Interface Prediction.py
├── templates/
│   └── index.html
├── Capstone Project PPT.key
├── Capstone Project - Video explanation .pdf
└── README.md

### ⚠️ Important: Flask automatically looks for HTML files inside a folder named templates.
Make sure index.html is placed there, otherwise the app will not render properly.

### Both housing_predictor.py and User Interface Prediction.py should remain in the same directory — they work together to process inputs, run predictions, and display results through Flask.

---

## 🚀 How to Run the Project
### 1. Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd week-2

### 3. Install dependencies:
pip install -r requirements.txt

### 4. Run the Flask app
python housing_predictor.py

### 5. Open in your browser
➡️ http://127.0.0.1:5000/

### 6. Stop the server
Press CTRL + C in your terminal to stop the app.

---

## 📊 Key Insights
1. Overall Quality and GrLivArea are the most influential features.
2. Houses with larger garages and recent renovations tend to have higher prices.
3. The model achieves an R² score of ~0.88, showing good predictive performance.

---

## 🏁 Conclusion
1. This capstone demonstrates a complete data science workflow — from raw data exploration to model deployment via a web app.
2. It highlights skills in data cleaning, visualization, model building, and Flask integration, providing a solid foundation for real-world machine learning applications.

---

# Author: Shivali Muthukumar | Data Analyst

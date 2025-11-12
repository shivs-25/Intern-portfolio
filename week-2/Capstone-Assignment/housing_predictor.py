#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the cleaned Dataset
df_cleaned = pd.read_csv("/Users/shivalimuthukumar/Desktop/mydrive/AmesHousing.csv")

# Select the important features
common_features_list = ['Lot Frontage', 'Lot Area', 'Overall Qual', 'Year Built',
       'Year Remod/Add', 'Mas Vnr Area', 'BsmtFin SF 1','Gr Liv Area','Garage Cars', 'Garage Area','SalePrice']

# Remove rows with NA values in the selected features
df_cleaned = df_cleaned[common_features_list].dropna()

# Prepare the data
x = df_cleaned[common_features_list].drop('SalePrice', axis = 1)
y = df_cleaned['SalePrice']

# Split data into Training and Testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

# Train the Gradient Boosting model
model = GradientBoostingRegressor(random_state = 42)
model.fit(x_train, y_train)

@app.route('/', methods=['GET' , 'POST'])
def index():
    prediction = None
    if request.method == 'POST' :
        # Get user input from the form
        lot_frontage = float(request.form['lot_frontage'])
        lot_area = float(request.form['lot_area'])
        overall_qual = int(request.form['overall_qual'])
        year_built = int(request.form['year_built'])
        year_remod_add = int(request.form['year_remod_add'])
        mas_vnr_area = float(request.form['mas_vnr_area'])
        bsmtfin_sf1 = float(request.form['bsmtfin_sf1'])
        gr_liv_area = float(request.form['gr_liv_area'])
        garage_cars = int(request.form['garage_cars'])
        garage_area = float(request.form['garage_area'])
        
        # Create a feature vector based on user input
        user_input = np.array([[lot_frontage, lot_area, overall_qual, year_built,
                            year_remod_add, mas_vnr_area, bsmtfin_sf1, 
                            gr_liv_area, garage_cars, garage_area]])
        
        # Predict the Housing Price based on user input
        prediction = model.predict(user_input)[0]
        
    return render_template('index.html', prediction = prediction)

if __name__ == '__main__' :
    app.run(debug = True) # will run in development environment
    
# Templates will contain index.html
# New directory for project: Python project
# Store python file
# Create a subfolder - templates


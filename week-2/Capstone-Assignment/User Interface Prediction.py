#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import ipywidgets as widgets
from IPython.display import display

print("1. Loading the cleaned datset\n")

df_cleaned = pd.read_csv("/Users/shivalimuthukumar/Desktop/mydrive/AmesHousing.csv")

print("2. Selecting Important Features\n")
common_features_list = ['Lot Frontage', 'Lot Area', 'Overall Qual', 'Year Built',
       'Year Remod/Add', 'Mas Vnr Area', 'BsmtFin SF 1','Gr Liv Area','Garage Cars', 'Garage Area','SalePrice']

print("3. Remove rows with NA values in the selected features\n")
df_cleaned = df_cleaned[common_features_list].dropna()

print("4. Define Features and Target variable\n")
x = df_cleaned[common_features_list].drop('SalePrice', axis = 1)
y = df_cleaned['SalePrice']

print("5. Split Data into Training and Testing sets\n")
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

print("6. Train the Gradient Boosting Model\n")
model = GradientBoostingRegressor(random_state = 42)
model.fit(x_train, y_train)

print("7. Create Widgets for user input\n")
lot_frontage = widgets.FloatSlider(value = 60, min=0, max=200, step = 1, description = 'Lot Frontage')
lot_area = widgets.FloatSlider(value = 10000, min=0, max=200000, step=100, description = 'Lot Area')
overall_qual = widgets.IntSlider(value = 5, min=1, max=10, description = 'Overall Quality')
year_built = widgets.IntSlider(value = 2000, min=1800, max=2024, description = 'Year Built')
year_remod_add = widgets.IntSlider(value = 2005, min=1800, max=2024, description = 'Year Remodeled')
mas_vnr_area = widgets.FloatSlider(value = 100, min=0, max=5000, step=1, description = 'Masonry Area')
bsmtfin_sf1 = widgets.FloatSlider(value = 500, min=0, max=2000, step = 1, description = 'Finished Basement')
gr_liv_area = widgets.FloatSlider(value = 1500, min=0, max=4000, step=1, description = 'Living Area')
garage_cars = widgets.IntSlider(value = 2, min=0, max=5, description = 'Garage Cars')
garage_area = widgets.FloatSlider(value = 500, min = 0, max=1500, step = 1, description = 'Garage Area')

print("8. Create a button for prediction\n")
predict_button = widgets.Button(description = 'Predict Housing Price')

print("9. Function to handle Button Click\n")
def on_button_clicked(b):
    user_input = np.array([[lot_frontage.value, lot_area.value, overall_qual.value, year_built.value,
                            year_remod_add.value, mas_vnr_area.value, bsmtfin_sf1.value, 
                            gr_liv_area.value, garage_cars.value, garage_area.value]])
    prediction = model.predict(user_input)[0]
    print(f"The prediction price is: ${prediction:,.2f}")
    

# Bind Button click event

predict_button.on_click(on_button_clicked)

print("10. Display the Widgets\n")
display(lot_frontage, lot_area, overall_qual, year_built,
        year_remod_add, mas_vnr_area, bsmtfin_sf1, 
        gr_liv_area, garage_cars, garage_area, predict_button)


# In[ ]:





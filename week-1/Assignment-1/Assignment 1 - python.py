#!/usr/bin/env python
# coding: utf-8

# In[24]:


print("1. Basic Data Types and Operations\n")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b if b != 0 else "Cannot divide by zero!")


# In[25]:


print("2. List Operations\n")

import random
numbers = [random.randint(1,100) for _ in range(10)]
print("My list: ")
for num in numbers :
    print(num)

print("The Ascending order of my list is: ", sorted(numbers))
print("The Descending order of my list is: ", sorted(numbers , reverse = True))
print("Minimum value of the list: ", min(numbers))
print("Maximum value of the list: ", max(numbers))
print("Average: ", sum(numbers) / len(numbers))


# In[26]:


print("3. Dictionary Operations\n")

students = {"John": 85, "Anna": 92, "Seth": 78, "Shivali":95, "Sanjana":88}
print("Student Names:", list(students.keys()))
print("Final grades:", list(students.values()))
top_student = max(students)
print("The top student for this exam is", top_student, "with the grades", students[top_student])


# In[27]:


print("4. String Manipulation\n")

sentence = input("Enter a sentence: ")

print("Uppercase: ", sentence.upper())

vowels = "aeiouAEIOU"
count = sum(1 for ch in sentence if ch in vowels)
print("Number of vowels:", count)

print("Reversed:", sentence[::-1])


# In[28]:


print("5. NumPy Array Basics\n")
import numpy as np

arr = np.arange(1, 11)
print("Original Array:", arr)

reshaped = arr.reshape(2,5)
print("Reshaped 2x5: \n", reshaped)

print("Mean: ", np.mean(arr))
print("Median", np.median(arr))
print("Standard Deviation", np.std(arr))

print("Even Indices Elements: ", arr[::2])


# In[29]:


print("6. Pandas DataFrame Creation\n")
import pandas as pd

data = {"Name" : ["John","Shivali","Sanjana"], "Age": [28, 24, 21], "Salary": [50000, 70000, 65000]}
df = pd.DataFrame(data)
print("First Two Rows: \n", df.head(2))

df["Department"] = ["HR", "IT", "Finance"]
print("\n After Dropping Age Column: \n", df)


# In[30]:


print("7. Reading and Writing CSV Files\n")

# Creating a CSV file
df.to_csv("employees.csv", index = False)

# Reading the CSV File
df_read = pd.read_csv("employees.csv")
print("First 5 Rows: \n", df_read.head())

#Modify salary (increase by 10%)
df_read["Salary"] = df_read["Salary"] * 1.1
df_read.to_csv("emplyees_updated.csv", index = False)
print("\nUpdated CSV saved as employees_updated.csv")


# In[32]:


print("8. Group by Operations\n")
data = {
    "Department" : ["HR", "IT", "Finance", "HR", "IT"],
    "Employee": ["John", "Shivali","Sanjana", "Sujatha", "Muthu"],
    "Salary" : [50000,70000,65000,68000,62000]
}
df_group = (pd.DataFrame(data))

grouped = df_group.groupby("Department")["Salary"].mean()
print("Average Salary by Department:\n", grouped)


# In[33]:


print("9. Data-Time Operations\n")

dates = pd.DataFrame({
    "Date" : pd.to_datetime(["2024-06-13","2024-08-11","2024-09-17","2024-12-25"])
})
print(dates)

dates["Year"] = dates["Date"].dt.year
dates["Month"] = dates["Date"].dt.month
dates["Day"] = dates["Date"].dt.day
print("\nWith Year, Month and Day:\n", dates)

diff = dates["Date"].iloc[2] - dates["Date"].iloc[0]
print("\nDifference between last and first date:", diff)


# In[37]:


print("10. Handling Missing Data\n")

data = {
    "Name": ["Shivali", "Sanjana", "Sujatha", "Muthu"],
    "Age" : [24, None, 28, None],
    "Salary" : [70000, 65000, 68000, None]
}
df_missing = pd.DataFrame(data)
print("Original Data Frame with Missing Values:\n", df_missing)

print("\nMissing Values:\n", df_missing.isnull())

df_missing["Age"].fillna(df_missing["Age"].mean(), inplace = True)
df_missing["Salary"].fillna(df_missing["Salary"].mean(), inplace = True)
print("\nAfter Filling the Missing Values:\n", df_missing)

df_clean = df_missing.dropna()
print("\nAfter Dropping Remaining Missing Values:\n", df_clean)


# In[ ]:





import pandas as pd

data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Location": ["New York", "Paris", "Berlin", "London"],
    "Age": [1, 2, 3, 4],
    "Salary": [70000, 80000, 120000, 90000],
    "Performance": [80, 90, 85, 95],
}

df = pd.DataFrame(data)
print("---Sample DataFrame---")
print(df)
print("\n---DataFrame Description---")
print(df.describe())
# mean = average (a+b)/2
# for learn do chatGPT std
# std = standard deviation (Sample Std) 
# min = minimum value in the column
# 25% = first quartile (Q1) - 25% of the data is below this value
# 50% = median (Q2) - 50% of the data is below this value
# 75% = third quartile (Q3) - 75% of the data is below this value
# max = maximum value in the column
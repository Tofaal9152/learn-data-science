import pandas as pd

data ={
    "Name": ["John", "Tofaal", "Peter", "Linda"],
    "Age": [20, None, 30, 35],
    "City": ["New York", "Paris", "Tangail", "London"],
    "Salary": [23, 80000, 120000, 95000]
}
df= pd.DataFrame(data)
print(df)

print("After interpolation missing data with fill")

# Linear work is done by default
df["Age"] = df["Age"].interpolate(method='linear')

print(df)


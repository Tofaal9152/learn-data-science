import pandas as pd

data ={
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, None],
    "City": ["New York", "Paris", None, "London"],
    "Salary": [23, 80000, 120000, 95000]
}
df= pd.DataFrame(data)
print(df)

print("After handling missing data with fill")

# df.fillna(0, inplace=True)
# df["Age"].fillna(df["Age"].mean(),inplace=True)


print(df)
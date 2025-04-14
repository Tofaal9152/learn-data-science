import pandas as pd

data ={
    "Name": ["John", "Anna", "beter", "Linda"],
    "Age": [28, 24, "35", 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 95000]
}
df= pd.DataFrame(data)
print(df)

# sorting 
print("After")

# print(df['Age'].sum())
# print(df['Age'].count())
# print(df['Age'].mean())
# print(df['Age'].min())
# print(df['Age'].max())
# print(df['Age'].median())
# print(df['Age'].std())
# print(df['Age'].describe())
# print(df['Age'].mode())

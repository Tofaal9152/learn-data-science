import pandas as pd

data ={
    "Name": ["John", "anna", "anna", "Linda","Tofaal"],
    "Age": [28, 24, 21, 32,21],
    "City": ["New York", "Paris", "Berlin", "London","Japan"],
    "Salary": [70000, 80000, 200000, 95000, 5000000]
}
df= pd.DataFrame(data)
# print(df)

# group
# print("After ")

# grouped=df.groupby("Age")["Salary"].sum()
# print(grouped)

grouped=df.groupby(["Name","Age"])["Salary"].describe()
print(grouped)
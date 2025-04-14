import pandas as pd

data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 95000]
}
df= pd.DataFrame(data)

print(df)

# print("Removing a column")
# df.drop("Name",axis=1,inplace=True)
# print(df)

# print("Removing a column")
# df.drop(columns=["Name","Age"],inplace=True)
# print(df)
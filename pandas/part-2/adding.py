import pandas as pd

data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 95000]
}
df= pd.DataFrame(data)
# print(df)

# #  adding a new column
# df["Country"] = ["USA", "France", "Germany", "UK"]
# df["Bonus"]=df["Salary"] * 0.1
# print(df)

# # Inserting a new column at a specific position
# df.insert(0,"Id",[1,2,3,4])

# # Adding a new column based on a condition
# df["Salary"] = df["Salary"].apply(lambda x: x*0.1 if x>8000 else x*0.05)

print(df)
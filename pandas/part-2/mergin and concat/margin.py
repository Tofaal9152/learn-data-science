import pandas as pd

data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 95000]
}
df= pd.DataFrame(data)

print(df)
print("After merging")
# Merging two dataframes
data2 = {
    "Name": ["John", "Anna", "Peter", "tofa"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 5000]
}
df2= pd.DataFrame(data2)

# Merge two dataframes
df3 = pd.merge(df, df2, on="Name", how="inner") 
print(df3)
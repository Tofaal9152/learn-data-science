import pandas as pd

data ={
    "Name": ["John", "Anna", "beter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 95000]
}
df= pd.DataFrame(data)
print(df)

# sorting 
print("After sorting")


# df.sort_values(by="Name",ascending=True,inplace=True)
# print(df)

# sorting by multiple columns
# df.sort_values(by=["Age"],ascending=[True],inplace=True)
# print(df)

# sorting multiple columns
# df.sort_values(by=["Name","Age"],ascending=[True,True],inplace=True)
# print(df)
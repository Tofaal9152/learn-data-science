import pandas as pd

data ={
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, None],
    "City": ["New York", "Paris", None, "London"],
    "Salary": [23, 80000, 120000, 95000]
}
df= pd.DataFrame(data)
print(df)

print("After handling missing data")

# # Drop rows with any missing values (if a none found in any rows it will be dropped)
# df.dropna(axis=0, how='any', inplace=True)

## Drop rows with all missing values (if a none found in all rows it will be dropped)
# df.dropna(axis=0, how='all', inplace=True)

# # Drop columns with any missing values (if a none found in any columns it will be dropped)
# df.dropna(axis=1, how='any', inplace=True) 

# Drop rows with all missing values (if a none found in all rows it will be dropped)
# df.dropna(axis=0, how='all', inplace=True) 



print(df)
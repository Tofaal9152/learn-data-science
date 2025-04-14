import pandas as pd

data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 95000]
}
df1= pd.DataFrame(data)

print("After concatenation")
# Merging two dataframes
data2 = {
    "Name": ["John", "Anna", "Peter", "tofa"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
    "Salary": [70000, 80000, 120000, 5000]
}
df2= pd.DataFrame(data2)

# concat
df3= pd.concat([df1,df2],axis=0,ignore_index=True)

print(df3)
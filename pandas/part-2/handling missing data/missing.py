import pandas as pd

data ={
    "Name": ["John", None, "Peter", "Linda"],
    "Age": [28, None, 35, None],
    "City": ["New York", "Paris", None, "London"],
    "Salary": [None, 80000, 120000, 95000]
}
df= pd.DataFrame(data)

print(df.isnull().sum())
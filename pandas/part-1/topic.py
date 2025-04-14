import pandas as pd

df= pd.read_json("./sample_data/json/sample_Data.json")

print(df)

# shape
print("Shape of the data")
print(df.shape)

# columns
print("Columns of the data")
print(df.columns)
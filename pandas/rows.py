import pandas as pd

df= pd.read_json("./sample_data/json/sample_Data.json")

# display 1st 10 raws of the data
print("Display 1st 10 rows of the data")
print(df.head())
# display last 10 raws of the data
print("Display Last 10 rows of the data")
print(df.tail())
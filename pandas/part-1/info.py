import pandas as pd

df = pd.read_json("./sample_data/json/sample_Data.json")


print("Display the info of data set")
print(df.info())
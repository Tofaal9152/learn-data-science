import pandas as pd
# df stand for data frame
# read data from csv 
# df_csv = pd.read_csv("sales_data_sample.csv",encoding="latin1")
# df_xlsx = pd.read_excel("1.xlsx")
df_json = pd.read_json("./sample_data/json/sample_Data.json")
print(df_json.applymap(type))
print(df_json)
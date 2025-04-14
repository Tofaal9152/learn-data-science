import pandas as pd

data ={
    "Name":["tofa","naiem","sami"],
    "Age":[22,23,24],
    "City":["Dhaka","Chittagong","Khulna"],
}
    
df=pd.DataFrame(data)

print(df)

df.to_csv("./sample_data/json/output.csv",index=False)
df.to_json("./sample_data/json/output.json",orient="records")
df.to_excel("./sample_data/json/output.xlsx",index=False)
import pandas as pd
import numpy as np

df = pd.read_csv("D:\\Cse\\learn-data-science\\Numpy\\project\\data.csv")
print(df)
# Clean the Salary column
df['Salary (INR)'] = pd.to_numeric(df['Salary (INR)'], errors='coerce')
df['Performance Rating'] = pd.to_numeric(df['Performance Rating'], errors='coerce')
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].mean())

lower_bound = df['Salary (INR)'].mean() - 3 * df['Salary (INR)'].std()
upper_bound = df['Salary (INR)'].mean() + 3 * df['Salary (INR)'].std()
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

df.replace([np.inf, -np.inf], np.nan, inplace=True) 
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())


print(df)

# save the cleaned data to a new CSV file
df.to_csv("D:\\Cse\\learn-data-science\\Numpy\\project\\cleaned_data.csv", index=False)


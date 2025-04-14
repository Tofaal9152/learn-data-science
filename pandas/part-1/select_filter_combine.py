import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [16, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 90, 88, 76, 95]
}

df = pd.DataFrame(data)
print(df)
# # Select specific columns
# selected_colums= df[['Name','Age']]
# print("\nSelected Columns:")
# print(selected_colums)
# print(df['Name'])

# Filter rows based on a condition
# filtered_rows = df[(df['Age']>18) & (df['Age']<30)].sort_values(by='Age', ascending=True)
# print("\nFiltered Rows")
# print(filtered_rows)

# # filter by multiple conditions
# filtered_rows = df[(df['Age'] > 18) | (df['City'] == 'New York')]
# print("\nFiltered Rows with multiple conditions:")
# print(filtered_rows)

# Combine two DataFrames (concatenation)
# additional_data = {
#     'Name': ['Frank', 'Grace'],
#     'Age': [30, 28],
#     'City': ['Seattle', 'Denver'],
#     'Score': [89, 92]
# }
# df_additional = pd.DataFrame(additional_data)

# combined_df = pd.concat([df,df_additional], ignore_index=True)
# print("\nCombined DataFrame:")
# print(combined_df)
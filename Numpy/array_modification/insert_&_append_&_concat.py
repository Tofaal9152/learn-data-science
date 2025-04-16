import pandas as pd
import numpy as np

sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price']).astype(int)
print("prices as numpy array:\n")
print(prices_np)

print("\nAfter\n")
new_arr = np.insert(prices_np,0,[1,2,3])
new_arr = np.append(new_arr,[1,2,3])
print(new_arr)

# concatenate two arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)




# list1=[1,2,3]
# list2=[4,5,6]

# result = [x+y for x,y  in zip(list1, list2)]
# print(result)

import pandas as pd
import numpy as np

sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price']).astype(int)
split =np.split(prices_np, 2) # split the array into 2 parts along the first axis (rows)
print("prices as numpy array:\n")
print(split)

print("\nAfter\n")

print(split[0]+split[1]) # add the two parts together

arr1 =np.array([1,2,3])
arr2 =np.array([4,5,6])
result = arr1 + arr2
print(result) # add the two arrays together

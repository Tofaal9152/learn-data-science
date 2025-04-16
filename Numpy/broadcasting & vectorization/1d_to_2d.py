import pandas as pd
import numpy as np

sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price']).astype(int).reshape(5, 4) 
print("prices as numpy array:\n")
print(prices_np)


print("\nAfter\n") 
discount_arr = np.array([1,2,3,4])
print(prices_np+discount_arr)



import pandas as pd
import numpy as np

sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price']).astype(int).reshape(5,4)
print("prices as numpy array:\n")
print(prices_np)
print(prices_np.shape)

print("\nAfter\n")
inser_2d_1 = np.insert(prices_np,0,[3,2,3,4,3], axis=1)
inser_2d_0 = np.insert(inser_2d_1,0,[4,2,3,4,3], axis=0)
print(inser_2d_1)
print(inser_2d_0)




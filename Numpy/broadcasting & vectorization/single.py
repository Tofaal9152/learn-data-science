import pandas as pd
import numpy as np

sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price']).astype(int)
print("prices as numpy array:\n")
print(prices_np)


print("\nAfter\n")
final_prices = prices_np * 0.9 # apply a 10% discount to all prices
print(final_prices)



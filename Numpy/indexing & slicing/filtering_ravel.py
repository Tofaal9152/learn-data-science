import random
import math
import pandas as pd
import numpy as np

df = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(df['price']).astype(int)
print("prices as numpy array:\n")
print(prices_np)

print("\nAfter\n")
print(prices_np[prices_np > 500])




import random
import math
import pandas as pd
import numpy as np

# list = [math.ceil(random.random()*100) for _ in range(10000)] 
# numpy_array = np.array(list)
# print(numpy_array)

sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price'])
print(prices_np.mean())



import random
import math
import pandas as pd
import numpy as np


sample_csv_json = pd.read_json('./sample_data/json/sample_Data.json')

prices_np= np.array(sample_csv_json['price'])
print(prices_np[-1])



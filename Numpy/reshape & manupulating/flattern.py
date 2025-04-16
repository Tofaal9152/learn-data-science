import pandas as pd
import numpy as np

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
b = a.flatten() # flatten is a copy of the original array
c= a.ravel() # ravel is a view of the original array
c[0] = 100
b[0] = 200
print(b)  
print(c) 
print(a) 





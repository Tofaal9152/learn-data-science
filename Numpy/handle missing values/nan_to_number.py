import numpy as np

arr= np.array([1,np.nan,2,3])

nantonum = np.nan_to_num(arr, nan=0) # replace NaN with 0
print(nantonum)  # Check the type of the object
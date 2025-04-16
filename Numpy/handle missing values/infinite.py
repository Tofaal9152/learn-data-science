import numpy as np

arr= np.array([1,np.nan,2,3,np.inf])


print(np.isinf(arr))  # Check the type of the object

# replace
cleaned_arr = np.nan_to_num(arr, nan=0, posinf=0, neginf=0)  # replace NaN and inf with 0
print(cleaned_arr)  # Check the type of the object
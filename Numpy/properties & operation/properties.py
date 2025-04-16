import numpy as np

arr_2d=[[1,2,3],
         [4,5,6],
            [7,8,9.4]]

numpy_arr_2d=np.array(arr_2d)
print(numpy_arr_2d)

# print the shape of the numpy array
print(numpy_arr_2d.shape)

# print the size of the numpy array
print(numpy_arr_2d.size)

# print the number of dimensions of the numpy array
print(numpy_arr_2d.ndim)

# print the data type of the numpy array
print(numpy_arr_2d.dtype)

# print the item size of the numpy array
print(numpy_arr_2d.itemsize) # it returns the size of each element in bytes

# print the total size of the numpy array
print(numpy_arr_2d.nbytes) # it returns the total size of the array in bytes

# type conversion
# convert the data type of the numpy array to sting
numpy_arr_2d_float=numpy_arr_2d.astype(str)
print(numpy_arr_2d_float)

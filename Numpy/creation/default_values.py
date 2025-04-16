# create a numpy array with default values
import numpy as np


# create a list with zeroes

zero_array = np.zeros(10)
print(zero_array)


# create a list with ones
one_array = np.ones((3,2))
print(one_array)

# cretae a list with a constant value
constant_array = np.full(3, 7)
# constant_array = np.full((6,4,2), 7)
print(constant_array)
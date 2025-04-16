
import numpy as np



arr1= np.array([1,2,3])
arr2 = np.array([4,5,6])

print("\nAfter\n")

print(np.stack((arr1, arr2), axis=0))
print(np.stack((arr1, arr2), axis=1))



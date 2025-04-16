import random
import math
import numpy as np
list = [math.ceil(random.random()*100) for _ in range(10000)] 

numpy_array = np.array(list)
print(numpy_array)


print(np.__version__)




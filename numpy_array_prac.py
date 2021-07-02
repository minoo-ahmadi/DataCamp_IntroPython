python_list = [1, 2, 3]
print(python_list)

import numpy as np
numpy_array = np.array(python_list)
print(numpy_array)

# calculations on numpy arrays are element-wise (compare to python lists). 
print (python_list + python_list)
print (numpy_array + numpy_array)

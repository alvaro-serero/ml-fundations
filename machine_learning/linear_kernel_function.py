"""Linear Kernel Function"""

import numpy as np

def kernel_function(x1, x2):
    return sum(x1[i] * x2[i] for i in range(len(x1)))


x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
result = kernel_function(x1, x2)
print(result)


# Simpler version using NumPy
def kernel_function_numpy(x1, x2):
    return np.dot(x1, x2)


result_2 = kernel_function_numpy(x1, x2)
print(result)
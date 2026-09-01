"""Convert Vector to Diagonal Matrix"""

import numpy as np

def make_diagonal(x):
	n = len(x)
	M = np.zeros((n, n))
	for i in range(n):
		M[i, i] = x[i] 
	return M

print(make_diagonal(np.array([1, 2, 3])))
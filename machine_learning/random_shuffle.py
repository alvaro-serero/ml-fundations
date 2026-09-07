"""Random Shuffle of Dataset"""

import numpy as np

def shuffle_data(X, y, seed=None):
	m = X.shape[0]
	if seed is not None:
		np.random.seed(seed)
	indices = np.random.permutation(m)
	X_shuffled = X[indices]
	y_shuffled = y[indices]
		
	return (X_shuffled, y_shuffled)


print(shuffle_data(np.array([[1, 2], [3, 4], [5, 6], [7, 8]]), np.array([1, 2, 3, 4]), seed=42))

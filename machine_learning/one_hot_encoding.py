"""One-Hot Encoding of Nominal Values"""

import numpy as np

def to_categorical(x, n_col=None):
	if n_col is None:
		n_col = np.max(x) + 1
	
	one_hot = np.zeros((len(x), n_col))
	for i in range(len(x)):
		one_hot[i, x[i]] = 1
	
	return one_hot


print(to_categorical(np.array([0, 1, 2, 1, 0])))
print(to_categorical(np.array([3, 1, 2, 1, 3]), 4))
print(to_categorical(np.array([0, 0, 0])))
print(to_categorical(np.array([1, 2, 0]), 5))

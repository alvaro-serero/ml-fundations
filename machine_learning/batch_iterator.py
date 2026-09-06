"""Batch Iterator for Dataset"""

import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    n_samples = len(X)
    for start in range(0, n_samples, batch_size):
        end = start + batch_size
        X_batch = X[start:end].tolist()

        if y is not None:
            y_batch = y[start:end].tolist()
            yield [X_batch, y_batch]
        else:
            yield X_batch

print(list(batch_iterator(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), np.array([1, 2, 3, 4, 5]), batch_size=2)))
print(list(batch_iterator(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), batch_size=3)))
print(list(batch_iterator(np.array([[1], [2], [3]]), np.array([10, 20, 30]), batch_size=1)))
print(list(batch_iterator(np.array([[1, 0], [0, 1], [1, 1], [0, 0], [2, 2], [3, 3]]), batch_size=4)))

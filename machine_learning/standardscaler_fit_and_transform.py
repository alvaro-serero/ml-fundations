"""StandardScaler Fit and Transform"""

import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    mu = X_train.mean(axis=0)
    sigma = X_train.std(axis=0)
    sigma[sigma == 0] = 1.0
    return (X_test - mu) / sigma


X_train = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
X_test = np.array([[2.0, 3.0], [4.0, 5.0]])
print(np.round(standard_scaler(X_train, X_test), 4).tolist())
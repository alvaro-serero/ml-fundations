"""Calculate Root Mean Square Error (RMSE)"""

import numpy as np

def rmse(y_true, y_pred):
    # Check for invalid input types
    if not isinstance(y_true, np.ndarray) or not isinstance(y_pred, np.ndarray):
        raise TypeError("y_true and y_pred must be NumPy arrays")

    # Check for mismatched array shapes
    if y_true.shape != y_pred.shape:
        raise ValueError("y_true and y_pred must have the same shape")

    # Check for empty arrays
    if y_true.size == 0:
        raise ValueError("Input arrays cannot be empty")

    rmse_res = np.sqrt(np.mean((y_true - y_pred) ** 2))

    return round(rmse_res, 3)


# Test Case 1: Normal Case
y_true1 = np.array([3, -0.5, 2, 7])
y_pred1 = np.array([2.5, 0.0, 2, 8])
print(rmse(y_true1, y_pred1))

# Test Case 2: 2D Array
y_true2 = np.array([[0.5, 1], [-1, 1], [7, -6]])
y_pred2 = np.array([[0, 2], [-1, 2], [8, -5]])
print(rmse(y_true2, y_pred2))

# Test Case 3: Perfect predictions
y_true3 = np.array([[1, 2], [3, 4]])
y_pred3 = np.array([[1, 2], [3, 4]])
print(rmse(y_true3, y_pred3))
import numpy as np

def calculate_dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The dot product of the two vectors.
    """
    s = 0
    for i in range(len(vec1)):
        s += vec1[i] * vec2[i]
    return s


print(calculate_dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])))
print(calculate_dot_product(np.array([-1, 2, 3]), np.array([4, -5, 6])))


def calculate_dot_product_numpy(vec1: np.ndarray, vec2: np.ndarray):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The dot product of the two vectors.
    """
    return np.dot(vec1, vec2)
    # return np.sum(vec1 * vec2)


print(calculate_dot_product_numpy(np.array([1, 2, 3]), np.array([4, 5, 6])))
print(calculate_dot_product_numpy(np.array([-1, 2, 3]), np.array([4, -5, 6])))
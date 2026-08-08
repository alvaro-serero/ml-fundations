import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    v1 = np.array(v1, dtype=float)
    v2 = np.array(v2, dtype=float)

    if v1.size == 0 or v2.size == 0 or v1.shape != v2.shape:
        return -1

    dot_product = np.dot(v1, v2)
    v1_norm, v2_norm = np.sqrt(np.sum(v1 ** 2)), np.sqrt(np.sum(v2 ** 2))

    return dot_product / (v1_norm * v2_norm)


v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(round(cosine_similarity(v1, v2), 3))

v1 = np.array([1, 2, 3])
v2 = np.array([-1, -2, -3])
print(round(cosine_similarity(v1, v2), 3))

v1 = np.array([1, 0, 7])
v2 = np.array([0, 1, 3])
print(round(cosine_similarity(v1, v2), 3))
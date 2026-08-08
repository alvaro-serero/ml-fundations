def vector_sum(a: list[int | float], b: list[int | float]) -> list[int | float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.

    if len(a) != len(b):
        return -1

    return [v1 + v2 for v1, v2 in zip(a, b)]

print(vector_sum([1, 2, 3], [4, 5, 6]))


import numpy as np

def vector_sum_numpy(a, b):
    if len(a) != len(b):
        return -1
    return (np.array(a) + np.array(b)).tolist()

print(vector_sum_numpy([1, 2, 3], [4, 5, 6]))

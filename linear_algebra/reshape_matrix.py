"""Reshape Matrix"""
import numpy as np


def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	try:
		return np.array(a).reshape(new_shape).tolist()
	except ValueError:
		return []


print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))
print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 4)))
print(reshape_matrix([[1,2,3],[4,5,6]], (3, 2)))
print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (2, 4)))

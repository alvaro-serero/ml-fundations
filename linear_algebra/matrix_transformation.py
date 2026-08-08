"""Matrix Transformation"""
import numpy as np


def transform_matrix(A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]) -> list[
	list[int | float]]:
	A, T, S = np.array(A, dtype=float), np.array(T, dtype=float), np.array(S, dtype=float)
	if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		return -1

	return (np.linalg.inv(T) @ A @ S).tolist()


print(transform_matrix([[1, 2], [3, 4]], [[2, 0], [0, 2]], [[1, 1], [0, 1]]))
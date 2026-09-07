"""Transformation Matrix from Basis B to C"""

import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	C = np.array(C, dtype=float)
	B = np.array(B, dtype=float)
	P = np.linalg.inv(C) @ B
	return P


print([[round(v, 4) for v in row] for row in transform_basis([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 2.3, 3], [4.4, 25, 6], [7.4, 8, 9]])])
print([[round(v, 4) for v in row] for row in transform_basis([[1,0],[0,1]],[[1,2],[9,2]])])

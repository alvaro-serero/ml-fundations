"""Matrix Determinant & Trace"""

def determinant(matrix: list[list[float]]) -> float:
	n = len(matrix)
	if n == 1:
		return matrix[0][0]
	if n == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	
	det = 0.0
	for j in range(n):
		minor = [row[:j] + row[j+1:] for row in matrix[1:]]
		det += (-1) ** j * matrix[0][j] * determinant(minor)
	return det

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	n = len(matrix)
	trace = sum(matrix[i][i] for i in range(n))
	return (determinant(matrix), trace)


det, trace = matrix_determinant_and_trace([[1, 0], [0, 1]]); print(round(float(det), 4), round(float(trace), 4))
det, trace = matrix_determinant_and_trace([[2, 3], [1, 4]]); print(round(float(det), 4), round(float(trace), 4))
det, trace = matrix_determinant_and_trace([[1, 2, 3], [0, 1, 4], [5, 6, 0]]); print(round(float(det), 4), round(float(trace), 4))
det, trace = matrix_determinant_and_trace([[2, 4], [1, 2]]); print(round(float(det), 4), round(float(trace), 4))
det, trace = matrix_determinant_and_trace([[2, -1, 0], [1, 3, -2], [0, 1, 4]]); print(round(float(det), 4), round(float(trace), 4))

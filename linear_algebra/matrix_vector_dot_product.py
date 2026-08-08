"""Matrix-Vector Dot Product"""

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	n, m = len(a), len(a[0])

	if m != len(b):
		return -1

	l = []

	for i in range(n):
		sum = 0
		for j in range(m):
			sum += a[i][j] * b[j]
		l.append(sum)

	return l


print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
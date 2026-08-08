"""Calculate Eigenvalues of a Matrix"""
import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    (a, b), (c, d) = matrix
    trace = a + d
    det = a * d - b * c
    discriminant = math.sqrt(trace ** 2 - 4 * det)
    return [(trace + discriminant) / 2, (trace - discriminant) / 2]


print(calculate_eigenvalues([[2, 1], [1, 2]]))
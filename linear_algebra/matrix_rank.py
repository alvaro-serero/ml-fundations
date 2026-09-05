"""Matrix Rank"""

import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    A = np.array(A, dtype=float)
    m, n = A.shape
    rank = 0
    row = 0
    for col in range(n):
        if row >= m:
            break

        pivot_row = row + np.argmax(np.abs(A[row:, col]))

        if abs(A[pivot_row, col]) <= tol:
            continue

        A[[row, pivot_row]] = A[[pivot_row, row]]

        for r in range(row + 1, m):
            factor = A[r, col] / A[row, col]
            A[r] -= factor * A[row]

        rank += 1
        row += 1

    return rank


A = np.array([[1, 2], [3, 4]]); print(matrix_rank(A))
A = np.array([[1, 2], [2, 4]]); print(matrix_rank(A))
A = np.array([[0, 0], [0, 0]]); print(matrix_rank(A))
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]); print(matrix_rank(A))
A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]); print(matrix_rank(A))
A = np.array([[1, 2, 3], [4, 5, 6]]); print(matrix_rank(A))
A = np.array([[1, 2], [3, 4], [5, 6]]); print(matrix_rank(A))

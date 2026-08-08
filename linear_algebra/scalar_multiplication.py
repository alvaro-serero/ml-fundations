"""Scalar Multiplication of a Matrix"""

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    for row in matrix:
        for i in range(len(row)):
            row[i] *= scalar

    return matrix


# Nested comprehension alternative
def scalar_multiply_2(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return [[scalar * c for c in row] for row in matrix]


print(scalar_multiply([[1,2],[3,4]], 2))
print(scalar_multiply_2([[1,2],[3,4]], 2))
"""Calculate Mean by Row or Column"""

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == "column":
        for i in range(len(matrix[0])):
            s = 0
            for row in matrix:
                s += row[i]
            means.append(s / len(matrix))
    elif mode == "row":
        for row in matrix:
            s = 0
            for el in row:
                s += el
            means.append(s / len(row))

    return means

def calculate_matrix_mean_2(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        vectors = matrix
    elif mode == "column":
        vectors = zip(*matrix)
    else:
        raise ValueError(f"mode must be 'row' or 'column', got {mode!r}")
    return [sum(v) / len(v) for v in vectors]


print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'row'))

print(calculate_matrix_mean_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))
print(calculate_matrix_mean_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'row'))

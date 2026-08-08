"""Calculate Covariance Matrix"""

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    k = len(vectors)
    n = len(vectors[0])
    means = [sum(vector) / n for vector in vectors]
    cov_matrix = [[0.0] * k for _ in range(k)]

    for i in range(k):
        for j in range(i, k):
            s = sum((vectors[i][t] - means[i]) * (vectors[j][t] - means[j]) for t in range(n))
            cov_matrix[i][j] = cov_matrix[j][i] = s / (n - 1)

    return cov_matrix


print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]))

# symmetric, both features increasing in lockstep
assert calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]) == [[1.0, 1.0], [1.0, 1.0]]

# perfect negative relationship
assert calculate_covariance_matrix([[1, 2, 3], [3, 2, 1]]) == [[1.0, -1.0], [-1.0, 1.0]]

# a constant feature has zero variance and zero covariance with anything
assert calculate_covariance_matrix([[1, 2, 3], [5, 5, 5]]) == [[1.0, 0.0], [0.0, 0.0]]

# single feature reduces to a 1x1 variance
assert calculate_covariance_matrix([[1, 2, 3, 4]]) == [[1.6666666666666667]]

# scaling one feature by 2 scales its covariances by 2, its variance by 4
assert calculate_covariance_matrix([[1, 2, 3], [2, 4, 6]]) == [[1.0, 2.0], [2.0, 4.0]]
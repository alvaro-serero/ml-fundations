"""Matrix Multiplication"""

def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]]:
    if len(a[0]) != len(b):
        return -1

    m, n, p = len(a), len(b), len(b[0])
    c = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c


print(matrixmul([[1,2,3],[2,3,4],[5,6,7]],[[3,2,1],[4,3,2],[5,4,3]]))
print(matrixmul([[1,2], [2,4]], [[2,1], [3,4], [4,5]]))

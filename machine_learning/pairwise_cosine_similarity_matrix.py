"""Pairwise Cosine Similarity Matrix"""

import numpy as np

def cosine_similarity(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return np.dot(a, b) / (norm_a * norm_b)

def pairwise_cosine_similarity(X):
    X = np.asarray(X, dtype=np.float64)
    n = X.shape[0]
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            S[i, j] = cosine_similarity(X[i], X[j])
    
    return np.round(S, 4).tolist()

print(pairwise_cosine_similarity([[1, 0], [0, 1]]))
print(pairwise_cosine_similarity([[1, 1], [2, 2], [1, 0]]))
print(pairwise_cosine_similarity([[1, 2, 3]]))
print(pairwise_cosine_similarity([[0, 0], [1, 1]]))
print(pairwise_cosine_similarity([[1, 0, 0], [0, 1, 0], [1, 1, 0], [-1, 0, 0]]))


# Shorter Version

def pairwise_cosine_similarity_short(X):
    X = np.asarray(X, dtype=float)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    X_normed = X / norms
    X_normed = np.where(norms == 0, 0.0, X_normed)
    S = X_normed @ X_normed.T
    S = np.round(S, 4)
    return S.tolist()


print(pairwise_cosine_similarity_short([[1, 0], [0, 1]]))

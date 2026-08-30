"""L2 Normalization Along an Axis"""

import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    norms = np.sqrt(np.sum(x ** 2, axis=axis, keepdims=True) + eps)
    return (x / norms).tolist()


print([round(v, 4) for v in l2_normalize(np.array([3.0, 4.0]), axis=0)])
out = l2_normalize(np.array([[1.0, 2.0, 2.0], [0.0, 3.0, 4.0]]), axis=1)
print([[round(v, 4) for v in row] for row in out])
out = l2_normalize(np.array([[3.0, 0.0], [4.0, 0.0]]), axis=0)
print([[round(v, 4) for v in row] for row in out])
out = l2_normalize(np.array([0.0, 0.0, 0.0]), axis=0, eps=1e-12)
print([round(v, 4) for v in out])
out = l2_normalize(np.array([[1.0, 1.0], [1.0, 1.0]]), axis=-1)
print([[round(v, 4) for v in row] for row in out])

import numpy as np


def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    match norm_type:
        case "l1":
            return np.sum(np.abs(arr))
        case "l2" | "frobenius":
            return np.sqrt(np.sum(arr ** 2))
        case _:
            raise ValueError(f"Unknown norm type: {norm_type}")


print(compute_norm(np.array([1, -2, 3]), 'l1'))
print(compute_norm(np.array([3, 4]), 'l2'))
print(round(compute_norm(np.array([[1, 2], [3, 4]]), 'frobenius'), 4))

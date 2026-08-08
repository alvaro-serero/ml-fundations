"""Partial Derivatives of Multivariable Functions"""
import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
    """
    Compute partial derivatives of multivariable functions.

    Args:
        func_name: Function identifier
            'poly2d': f(x,y) = x²y + xy²
            'exp_sum': f(x,y) = e^(x+y)
            'product_sin': f(x,y) = x·sin(y)
            'poly3d': f(x,y,z) = x²y + yz²
            'squared_error': f(x,y) = (x-y)²
        point: Point (x, y) or (x, y, z) at which to evaluate

    Returns:
        Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
    """
    x, y, *maybe_z = point
    z = maybe_z[0] if maybe_z else 0

    match func_name:
        case 'poly2d':
            return (2 * x * y) + (y ** 2), (2 * x * y) + (x ** 2)
        case 'exp_sum':
            e = float(np.exp(x + y))
            return e, e
        case 'product_sin':
            return np.sin(y), np.cos(y) * x
        case 'poly3d':
            return 2 * x * y, x ** 2 + z ** 2, 2 * z * y
        case 'squared_error':
            return 2 * x - 2 * y, 2 * y - 2 * x

    raise ValueError(f"Unknown function: {func_name}")

result = compute_partial_derivatives('poly2d', (2.0, 3.0)); print(f"{result[0]:.1f},{result[1]:.1f}")
result = compute_partial_derivatives('exp_sum', (1.0, 0.0)); print(f"{result[0]:.6f}")
result = compute_partial_derivatives('product_sin', (2.0, 1.5708)); print(f"{result[0]:.4f},{result[1]:.4f}")
result = compute_partial_derivatives('poly3d', (1.0, 2.0, 3.0)); print(f"{result[0]:.1f},{result[1]:.1f},{result[2]:.1f}")
result = compute_partial_derivatives('squared_error', (5.0, 3.0)); print(f"{result[0]:.1f},{result[1]:.1f}")

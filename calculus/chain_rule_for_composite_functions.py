"""Chain Rule For Composite Functions"""
import numpy as np


def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.

    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative

    Returns:
        Derivative value at x

    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    val = float(x)
    grad = 1.0
    for name in reversed(functions):
        match name:
            case 'square':
                d, new = 2 * val, val ** 2
            case 'sin':
                d, new = np.cos(val), np.sin(val)
            case 'exp':
                d, new = np.exp(val), np.exp(val)
            case 'log':
                d, new = 1 / val, np.log(val)
            case _:
                raise ValueError(f"Unknown function: {name}")
        grad *= d
        val = new
    return float(grad)


result = compute_chain_rule_gradient(['sin', 'square'], 1.0); print(f"{result:.6f}")
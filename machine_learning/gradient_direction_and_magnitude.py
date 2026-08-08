"""Gradient Direction and Magnitude"""
import numpy as np


def gradient_direction_magnitude(gradient: list[float]) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.

    Args:
        gradient: A list representing the gradient vector

    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    g = np.array(gradient, dtype=float)
    magnitude = float(np.sqrt(np.sum(g ** 2)))

    if magnitude == 0.0:
        zeros = [0.0] * len(g)
        return {'magnitude': 0.0, 'direction': zeros, 'descent_direction': zeros}

    direction = g / magnitude
    return {
        'magnitude': magnitude,
        'direction': direction.tolist(),
        'descent_direction': (-direction).tolist(),
    }

result = gradient_direction_magnitude([3.0, 4.0])
print(f"{result['magnitude']:.4f},{[round(d,4) for d in result['direction']]},{[round(d,4) for d in result['descent_direction']]}")
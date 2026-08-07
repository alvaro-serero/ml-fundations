"""Single Neuron"""
import numpy as np


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    X = np.array(features, dtype=float)
    w = np.array(weights, dtype=float)
    y = np.array(labels, dtype=float)

    z = X @ w + bias
    probs = 1 / (1 + np.exp(-z))
    mse = np.mean((probs - y) ** 2)

    return probs, mse


print(single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1))
print(single_neuron_model([[1, 2], [2, 3], [3, 1]], [1, 0, 1], [0.5, -0.2], 0))
"""Single Neuron with Backpropagation"""
import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))


def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    features = np.array(features, dtype=float)
    labels = np.array(labels, dtype=float)
    weights = np.array(initial_weights, dtype=float)
    bias = float(initial_bias)
    mse_values = []
    n = len(labels)

    for _ in range(epochs):
        # Forward pass over all training examples with sigmoid activation
        z = features @ weights + bias
        sigma_z = sigmoid(z)

        # Compute MSE loss
        mse = np.mean((sigma_z - labels) ** 2)
        mse_values.append(round(float(mse), 4))

        # Backward pass (gradient calculation)
        delta = 2 * (sigma_z - labels) * sigma_z * (1 - sigma_z) / n  # shape (n,)
        d_w = features.T @ delta  # shape (d,)
        d_b = np.sum(delta)

        # Parameter update
        weights = weights - learning_rate * d_w
        bias = bias - learning_rate * d_b

    return np.round(weights, 4), round(bias, 4), mse_values


print(train_neuron(np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]]), np.array([1, 0, 0]), np.array([0.1, -0.2]), 0.0, 0.1, 2))
print(train_neuron(np.array([[1, 2], [2, 3], [3, 1]]), np.array([1, 0, 1]), np.array([0.5, -0.2]), 0, 0.1, 3))
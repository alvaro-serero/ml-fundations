"""Derivatives of Activation Functions"""

import numpy as np

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	sigmoid = 1 / (1 + np.exp(-x))
	sigmoid_derivative = sigmoid * (1 - sigmoid)
	tanh_derivative = 1 - np.tanh(x) ** 2
	relu_derivative = 1.0 if x > 0 else 0.0
	
	return {
		'sigmoid': sigmoid_derivative,
		'tanh': tanh_derivative,
		'relu': relu_derivative
    }


result = activation_derivatives(0.0)
print({k: round(v, 4) for k, v in result.items()})
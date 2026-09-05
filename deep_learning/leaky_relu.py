"""Leaky ReLU Activation Function"""

def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	return z if z > 0 else alpha * z


print(leaky_relu(5))
print(leaky_relu(1))
print(leaky_relu(-1))


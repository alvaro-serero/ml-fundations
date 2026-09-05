"""Implement ReLU Activation Function"""

def relu(z: float) -> float:
	return max(0.0, z)

print(relu(0.0))
print(relu(1.0))
print(relu(-1.0))

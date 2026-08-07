"""Sigmoid Activation Function"""
import math

def sigmoid(z: float) -> float:
	return 1 / (1 + math.exp(-z))

print(sigmoid(0))
print(sigmoid(1))
print(sigmoid(-1))

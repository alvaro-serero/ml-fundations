"""Calculate Accuracy Score"""

import numpy as np

def accuracy_score(y_true, y_pred):
	total = len(y_true)
	correct = np.sum(y_pred == y_true)
	return correct / total


print(accuracy_score(np.array([1, 0, 1, 1, 0, 1]), np.array([1, 0, 0, 1, 0, 1])))
print(accuracy_score(np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0])))
print(accuracy_score(np.array([1, 0, 1, 0, 1]), np.array([0, 1, 0, 1, 0])))


# Shorter version
def accuracy_score_short(y_true, y_pred):
	return np.mean(y_true == y_pred)


print(accuracy_score_short(np.array([1, 0, 1, 1, 0, 1]), np.array([1, 0, 0, 1, 0, 1])))
print(accuracy_score_short(np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0])))
print(accuracy_score_short(np.array([1, 0, 1, 0, 1]), np.array([0, 1, 0, 1, 0])))
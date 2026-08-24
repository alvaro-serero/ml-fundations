"""Feature Scaling Implementation"""

import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	data = np.asarray(data, dtype=float)
	mean = data.mean(axis=0)
	std = data.std(axis=0)
	standardized = (data - mean) / std

	mn = data.min(axis=0)
	mx = data.max(axis=0)
	normalized = (data - mn) / (mx - mn)
	return np.round(standardized, 4), np.round(normalized, 4)


print(feature_scaling(np.array([[1, 2], [3, 4], [5, 6]])))

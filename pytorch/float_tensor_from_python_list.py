"""Create a Float Tensor from a Python List"""

import torch

def to_float_tensor(values):
    return torch.tensor(values, dtype=torch.float32)


print(to_float_tensor([1, 2, 3]).tolist())

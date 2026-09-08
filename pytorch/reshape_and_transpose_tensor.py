"""Reshape and Transpose a Tensor"""

import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    return torch.reshape(x.flatten(), new_shape)

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    # TODO: swap the last two dimensions of x
    return torch.transpose(x, -1, -2)


x = torch.arange(6)
print(flatten_then_reshape(x, (2, 3)).tolist())

x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(transpose_last_two(x).tolist())

x = torch.zeros(2, 3, 4)
print(transpose_last_two(x).shape)

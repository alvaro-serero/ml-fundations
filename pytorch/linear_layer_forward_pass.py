"""Implement a Linear Layer Forward Pass with Matrix Multiplication"""

import torch

def linear_forward(x: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: implement y = x W^T + b using PyTorch ops
    return x @ W.T + b


x = torch.tensor([[1, 2]], dtype=torch.float)
W = torch.tensor([[1, 0], [0, 1], [1, 1]], dtype=torch.float)
b = torch.tensor([0, 0, 0], dtype=torch.float)
y = linear_forward(x, W, b)
print(y)

"""Add a Bias Vector to a Batch via Broadcasting"""

import torch

def add_bias(x: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # TODO: add b to every row of x using broadcasting
    return x + b


x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = torch.tensor([10.0, 20.0, 30.0])
print(add_bias(x, b).tolist())
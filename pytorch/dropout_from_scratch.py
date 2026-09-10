"""Implement Dropout from Scratch"""

import torch

def dropout(x: torch.Tensor, p: float, training: bool) -> torch.Tensor:
    # TODO: implement inverted dropout
    if not training:
        return x

    random_values = torch.rand_like(x)
    mask = random_values > p
    return x * mask / (1 - p)


torch.manual_seed(0)
x = torch.ones(8)
out = dropout(x, p=0.5, training=False)
print(torch.equal(out, x))

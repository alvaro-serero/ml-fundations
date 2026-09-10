"""Backprop a Linear Layer by Hand"""

import torch

def linear_backward(grad_output, x, W):
    # TODO: return (grad_input, grad_W, grad_b) for y = x @ W.T + b
    # Gradient w.r.t input
    grad_input = grad_output @ W

    # Gradient w.r.t weights
    grad_W = grad_output.T @ x

    # Gradient w.r.t bias
    grad_b = grad_output.sum(dim=0)

    return grad_input, grad_W, grad_b


grad_output = torch.tensor([[1.0, 1.0], [1.0, 1.0]])
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
W = torch.eye(2)
gi, gW, gb = linear_backward(grad_output, x, W)
print(gi.tolist())
print(gW.tolist())
print(gb.tolist())
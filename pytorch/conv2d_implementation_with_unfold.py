"""Implement Conv2d with `unfold`"""

import torch
import torch.nn.functional as F

def conv2d_via_unfold(x: torch.Tensor, W: torch.Tensor, b: torch.Tensor, stride=1, padding=0):
    # TODO: implement conv2d using F.unfold + matmul

    # Get shapes of x and W
    N, C_in, H, W_in = x.shape
    C_out, _, kH, kW = W.shape

    # Compute the height and width of the output
    H_out = (H + 2 * padding - kH) // stride + 1
    W_out = (W_in + 2 * padding - kW) // stride + 1

    # Get patches of shape (N, C_in * kH * kW, L)
    patches = F.unfold(x, kernel_size=(kH, kW), stride=stride, padding=padding)

    # Reshape weights to get the shape (C_out, C_in * kH * kW)
    W_flat = W.reshape((C_out, C_in * kH * kW))

    # Convolution output of shape (N, C_out, L)
    output = torch.matmul(W_flat, patches)

    # Add bias, broadcasting over N and spatial positions.
    output = output + b.view(1, C_out, 1)

    return output.reshape(N, C_out, H_out, W_out)


torch.manual_seed(0)
x = torch.randn(2, 3, 8, 8)
W = torch.randn(4, 3, 3, 3)
b = torch.randn(4)
out = conv2d_via_unfold(x, W, b, stride=1, padding=1)
ref = F.conv2d(x, W, b, stride=1, padding=1)
print(torch.allclose(out, ref, atol=1e-5))


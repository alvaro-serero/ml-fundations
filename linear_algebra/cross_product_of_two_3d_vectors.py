import numpy as np

"""
We are working with vectors in 3D space so we compute the cross product on 3 dimensions.
The cross product is defined by the determinant of the following matrix:

        | i   j   k  |
a x b = | a1  a2  a3 |
        | b1  b2  b3 |

For component i: a2b3 - a3b2
For component j: -(a1b3 - a3b1) = a3b1 - a1b3
For component k: a1b2 - a2b1

From this we can derive the general formula of the cross product for vecotrs in 3D space:
a * b = [a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1] 
"""

def cross_product(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]


print(cross_product([1, 0, 0], [0, 1, 0]))
print(cross_product([0, 1, 0], [0, 0, 1]))
print(cross_product([1, 2, 3], [4, 5, 6]))
print(cross_product([1, 0, 0], [1, 0, 0]))

"""Derivative of a Polynomial"""

def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * n * x ** (n-1)

print(poly_term_derivative(2.0, 3.0, 2.0))
print(poly_term_derivative(1.5, 4.0, 0.0))
print(poly_term_derivative(3.0, 2.0, 3.0))
print(poly_term_derivative(0.5, 5.0, 1.0))

import numpy as np

def poly_derivative(c: list) -> list:
    res = []

    for i in range(1, len(c)):
        res.append(i * c[i])

    return res

def poly_multiply(a: list, b: list) -> list:
    out = [0.0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out

def poly_add(a: list, b: list) -> list:
    m = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(m)]


def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.

    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i

    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    fp = poly_derivative(f_coeffs)
    gp = poly_derivative(g_coeffs)

    res = poly_add(poly_multiply(fp, g_coeffs), poly_multiply(f_coeffs, gp))
    return res if res else [0.0]


print(product_rule_derivative([1, 2], [3, 4]))
print(product_rule_derivative([3], [5]))


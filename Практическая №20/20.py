import math
import numpy as np

def compute_z(x):
    if x >= 0:
        return math.cos(x**5) + math.sin(x) * math.log(abs(x**2 + 1))
    else:
        return math.log(abs(x**2 + 1))

def compute_y(x):
    denominator = math.sin(2*x) + math.cos(x)
    if denominator == 0:
        raise ValueError("Деление на ноль в формуле y!")
    numerator = math.log(abs(math.sin(x)))
    if numerator <= 0:
        raise ValueError("Логарифм отрицательного числа в формуле y!")
    return (1 / (2 * math.pi * x)) * math.sqrt(numerator / denominator)

def compute_S(x_values):
    return sum(x_values)

def remainder(S, k):
    return S % k

def power(S, k):
    return S ** k

def gcd_poly(P, Q):
    return np.poly1d(np.gcd(P.c, Q.c))

def subtract_poly(P, Q):
    return P - Q
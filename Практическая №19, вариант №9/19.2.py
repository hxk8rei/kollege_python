import math

def compute_y(x):
    if x == 0:
        raise ValueError("x не может быть равно 0")
    
    sin_2x = math.sin(2 * x)
    cos_x = math.cos(x)
    
    if sin_2x <= 0:
        raise ValueError("sin(2x) должно быть больше 0")
    if 2 * x + cos_x <= 0:
        raise ValueError("2x + cos(x) должно быть больше 0")
    
    term1 = 1 / (2 * math.pi * x)**2
    numerator = math.log(sin_2x)
    denominator = math.log(2 * x + cos_x)
    y = term1 * (numerator / denominator)
    return y

x = 0.5  
try:
    result = compute_y(x)
    print(f"y = {result}")
except ValueError as e:
    print(f"Ошибка: {e}")
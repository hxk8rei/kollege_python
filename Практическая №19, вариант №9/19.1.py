import math

def compute_z(x, y):
    if x <= 0:
        raise ValueError("x должно быть больше 0")
    
    cos_x = math.cos(x)
    ln_x = math.log(x)
    part1 = (cos_x**5 + 0.5 + 10 * y) * (y / (ln_x + 2))
    determinant = 4 * (x**2 + 2) - ln_x
    z = part1 + determinant
    return z

x = 1.0
y = 1.0

try:
    result = compute_z(x, y)
    print(f"z = {result}")
except ValueError as e:
    print(f"Ошибка: {e}")
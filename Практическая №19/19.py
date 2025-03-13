import math
import numpy as np


def compute_z(x):
    if x >= 0:
        return math.cos(x ** 5) + math.sin(x) * math.log(abs(x ** 2 + 1))
    else:
        return math.log(abs(x ** 2 + 1))


def compute_y(x):
    denominator = math.sin(2 * x) + math.cos(x)
    if denominator == 0:
        raise ValueError("Деление на ноль в формуле y!")
    numerator = math.log(abs(math.sin(x)))
    if numerator <= 0:
        raise ValueError("Логарифм отрицательного числа в формуле y!")
    return (1 / (2 * math.pi * x)) * math.sqrt(numerator / denominator)


n = int(input("Введите n (количество членов): "))
k = int(input("Введите k (для остатка и степени): "))
x0 = float(input("Введите точку x0: "))

x_values = []
z_values = []
y_values = []

S = 0
for i in range(1, n + 1):
    x = float(input(f"Введите x({i}): "))
    x_values.append(x)
    S += x

    try:
        z = compute_z(x)
        y = compute_y(x)
        z_values.append(z)
        y_values.append(y)
    except ValueError as e:
        print(f"Ошибка при вычислении для x({i}): {e}")
        z_values.append(None)
        y_values.append(None)

print("\nСохраненные значения:")
for i in range(n):
    print(f"x({i + 1}) = {x_values[i]}, z({i + 1}) = {z_values[i]}, y({i + 1}) = {y_values[i]}")

print(f"\nСумма S = {S}")

remainder = S % k
print(f"Остаток от деления S на k: {remainder}")

power = S ** k
print(f"S в степени k: {power}")

print("Производная S: не определена, так как S - это число. Возможно, требуется производная z или y.")

S_x0 = 0
for i in range(1, n + 1):
    S_x0 += x0
print(f"Значение S в точке x0 (если подразумевается пересчет): {S_x0}")

P = np.poly1d([1, 2, 1])
Q = np.poly1d([1, 1])

gcd = np.poly1d(np.gcd(P.c, Q.c))
print(f"НОД полиномов P(x) и Q(x): {gcd}")

difference = P - Q
print(f"P(x) - Q(x): {difference}")
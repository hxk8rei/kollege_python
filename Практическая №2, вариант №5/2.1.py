# Григорьев Максим Денисович
# Вычислить значения по формулам при действительных значения всех переменных.

import math

try:
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    z = float(input("Введите значение z: "))
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    f = float(input("Введите значение f: "))
    
    result_1 = math.exp(x) - y**2 + 12*x*y - 3*x**2 / (18*y - 1)
    print("Первая формула:", result_1)

    result_2 = math.cos(x)**2 / math.sin(x) - x*y*z + a*x**2 + b*x + c / (x**3 - f)
    print("Вторая формула:", result_2)
except ValueError:
    print("Ошибка! Введите правильные числовые значения для переменных.")
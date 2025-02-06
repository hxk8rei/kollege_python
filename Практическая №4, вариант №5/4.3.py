while True:
    try:
        a = float(input("Введите начало отрезка a: "))
        b = float(input("Введите конец отрезка b: "))
        h = float(input("Введите шаг h: "))
        if h <= 0 or a >= b:
            print("Убедитесь, что b > a и h > 0.")
            continue
        break
    except ValueError:
        print("Введите числа.")

x = a
print(" x\tF(x)")

while x <= b:
    try:
        fx = 1 / (1 / (x) - 1)
        print(f"{x}\t{fx}")
    except ZeroDivisionError:
        print(f"{x}\tОшибка (деление на ноль)")
        x += h
    break
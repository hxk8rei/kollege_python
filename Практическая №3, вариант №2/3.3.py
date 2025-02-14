# Григорьев Максим Денисович
# Вычислить значение функций

while True:
    try:
        x = float(input("Введите значение x: "))

        if x > 3:
            result = -x**2 + 3*x + 9
        elif x < 3:
            result = x / (x**3 - 6)
        else:
            print("Ошибка! Введите x, не равный 3.")
            continue
        
        print(f"Значение функции F(x) = {result}.")
        break
    except ValueError:
        print("Ошибка! Введите правильное числовое значение для x.")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль.")
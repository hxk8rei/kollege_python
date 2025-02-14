# Григорьев Максим Денисович
# Дано действительное число R вида nnn.ddd (по три цифровых разряда в дробной и целой частях). Поменять местами дробную и целую части этого числа и вывести новое полученное число.

while True:
    try:
        R = input("Введите число R в формате nnn.ddd: ").strip()
        
        if not R:
            print("Ошибка! Вы не ввели число.")
            continue

        parts = R.split('.')
        if len(parts) != 2 or len(parts[1]) != 3:
            print("Ошибка! Число должно содержать три цифры после точки.")
            continue
        
        int_part = int(parts[0])
        frac_part = int(parts[1])

        new_R = f"{frac_part:03d}.{int_part}"
        print("Новое число после изменения частей:", new_R)
        break
    except ValueError:
        print("Ошибка! Введите число в правильном формате.")
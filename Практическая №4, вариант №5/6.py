while True:
    n = input("Введите натуральное число: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Введите корректное число.")

    
steps = 0
max_steps = 100

while True:
    str_n = str(n)
    reversed_str = str_n[::-1]

    if str_n == reversed_str:
        print(f"\nРезультат: {n} (палиндром за {steps} шага/шагов)")
        break

    if steps >= max_steps:
        print("Не удалось найти палиндром за допустимое количество шага/шагов")
        break

    reversed_n = int(reversed_str)
    sum_n = n + reversed_n

    print(f"{n} + {reversed_n} = {sum_n}")

    n = sum_n
    steps += 1
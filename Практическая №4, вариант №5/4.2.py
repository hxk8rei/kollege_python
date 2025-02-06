while True:
    try:
        n = int(input("Введите натуральное число n: "))
        if n <= 0:
            print("Введите натуральное число.")
            continue
        break
    except ValueError:
        print("Введите число.")

y = 1
i = 2
while i <= 2 * n:
    y = y * i
    i += 2

print("y =", y)
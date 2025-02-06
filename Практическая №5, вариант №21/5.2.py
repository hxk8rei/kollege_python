while True:
    try:
        N = int(input("Введите натуральное число N: "))
        if N <= 0:
            print("Введите натуральное число больше 0.")
            continue
        break
    except ValueError:
        print("Введите корректное число.")

for i in range(2, N):
    sum_divisors = 1
    for j in range(2, i):
        if i % j == 0:
            sum_divisors += j

    if sum_divisors == i:
        print(i)
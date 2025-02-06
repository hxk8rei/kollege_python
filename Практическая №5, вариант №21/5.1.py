while True:
    try:
        N = int(input("Введите натуральное число N (N > 9): "))
        if N <= 9:
            print("Введите число больше 9.")
            continue
        break
    except ValueError:
        print("Введите корректное число.")

count_zeros = 0

temp = N
digits = 0
while temp > 0:
    digits += 1
    temp = temp // 10

for i in range(2, digits + 1):
    power = 10 ** (digits - i)
    digit = (N // power) % 10
    if digit == 0:
        count_zeros += 1
    else:
        break 

print("Количество нулей в старших разрядах:", count_zeros)
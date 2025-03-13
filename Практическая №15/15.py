numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open('numbers.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + '\n')

even_sum = 0
with open('numbers.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        if num % 2 == 0:
            even_sum += num

print(f"Сумма четных чисел: {even_sum}")
matrix = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 9, -11]
]

max_sum = -1
result_row = None
for row in matrix:
    all_odd = True
    for num in row:
        if num % 2 == 0:
            all_odd = False
            break
    if all_odd:
        current_sum = sum(abs(num) for num in row)
        if current_sum > max_sum:
            max_sum = current_sum
            result_row = row
print("\nОтвет:")
if result_row is not None:
    print(f"Строка: {result_row}, Сумма модулей: {max_sum}")
else:
    print("Нет подходящих строк")
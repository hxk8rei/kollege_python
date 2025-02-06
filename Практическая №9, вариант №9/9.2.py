original = [15, 23, 34, 45, 55, 67, 75, 89]
k = 5

result = []
for number in original:
    if number % 10 == k:
        result.append(number)

print("Новый массив:", result)
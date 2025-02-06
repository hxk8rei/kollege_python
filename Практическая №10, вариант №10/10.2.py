matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k = 1
n = len(matrix)

if 0 <= k < n:
    diagonal = matrix[k][k]
    if diagonal != 0:
        for j in range(n):
            matrix[k][j] = matrix[k][j] / diagonal
    else:
        print("Ошибка: диагональный элемент равен нулю.")
else:
    print("Некорректный k.")
print("Ответ:")
for row in matrix:
    print([round(num, 2) for num in row])
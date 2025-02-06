x = [2, 3, 4]
n = len(x)
matrix = []
for i in range(n):
    row = [num ** (i + 1) for num in x]
    matrix.append(row)
print("Ответ:")
for row in matrix:
    print(row)
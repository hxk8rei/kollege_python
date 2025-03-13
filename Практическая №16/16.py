# Создаем модуль matrix_utils.py
with open('matrix_utils.py', 'w', encoding='utf-8') as f:
    f.write('''
def replace_values(matrix, znach1, znach2):
    return [[znach2 if x != znach1 else x for x in row] for row in matrix]
''')

import matrix_utils

A = [
    [1, 2, 3],
    [2, 4, 2],
    [5, 2, 6]
]

znach1 = 2
znach2 = 0

# Вывод исходной матрицы
print("Исходная матрица:")
for row in A:
    print(row)

result = matrix_utils.replace_values(A, znach1, znach2)

print("\nМатрица после замены:")
for row in result:
    print(row)
x = [2, 1, 4, 5, 6]
y = [2, 3, 5, 7]
z = [2, 5, 8, 9]

i = 0
j = 0
k = 0

found = False

while i < len(x) and j < len(y) and k < len(z):
    current_x = x[i]
    current_y = y[j]
    current_z = z[k]

    if current_x == current_y == current_z:
        print("Первое общее число:", current_x)
        found = True
        break

    min_elem = min(current_x, current_y, current_z)

    if current_x == min_elem:
        i += 1
    if current_y == min_elem:
        j += 1
    if current_z == min_elem:
        k += 1

if not found:
    print("Общего числа не найдено")
massiv = [1, 2 , 3, 4, 5, 6, 7, 8]

n = len(massiv) // 2
arguments = massiv[:n]
functions = massiv[n:]

print("Аргумент\tФункция")
for arg, func in zip(arguments, functions):
    print(f"{arg}\t\t{func}")
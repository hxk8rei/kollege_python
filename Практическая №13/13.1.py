import random

with open('file_f.txt', 'w') as f:
    for _ in range(20):
        f.write(str(random.randint(1, 100)) + '\n')

unique_numbers = set()
with open('file_f.txt', 'r') as f:
    for line in f:
        unique_numbers.add(int(line.strip()))

with open('file_g.txt', 'w') as g:
    for number in sorted(unique_numbers):
        g.write(str(number) + '\n')

print("Содержимое файла g (уникальные числа):")
with open('file_g.txt', 'r') as g:
    print(g.read())
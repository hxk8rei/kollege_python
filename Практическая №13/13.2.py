goods = [
    "Яблоки Россия 1000",
    "Бананы Китай 500",
    "Груши Франция 750"
]

with open('Tovar.txt', 'w', encoding='utf-8') as f:
    for line in goods:
        f.write(line + '\n')

print("Наименование\tСтрана\t\tОбъем")
print("-" * 40)
with open('Tovar.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, country, volume = line.strip().split()
        print(f"{name:<12}\t{country:<12}\t{volume}")
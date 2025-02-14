# Григорьев Максим Денисович
# В заданной строке между словами вставить вместо пробела запятую и пробел.

while True:
    input_string = input("Введите строку: ").strip()
    
    if not input_string:
        print("Ошибка! Строка не должна быть пустой.")
        continue

    modified_string = input_string.replace(" ", ", ")
    print("Модифицированная строка:", modified_string)
    break
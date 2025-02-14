# Григорьев Максим Денисович
# Составить программу, печатающую значение True, если следующие указанные высказывания являются истинными, и значение false — в противном случае. Только один из двух введенных символов не является цифрой.

while True:
    input_string = input("Введите строку для проверки, состоит ли она из цифр: ").strip()
    
    if not input_string:
        print("Ошибка! Вы не ввели строку.")
        continue

    is_all_digits = all(char.isdigit() for char in input_string)
    print("Все ли символы цифры:", is_all_digits)
    break
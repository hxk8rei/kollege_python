def to_decimal(number_str, base):
    decimal = 0
    for digit in number_str:
        digit_value = int(digit)
        decimal = decimal * base + digit_value
    return decimal

number_str = input("Введите число в p-ичной системе счисления: ")
base = int(input("Введите основание системы счисления (2 <= p <= 9): "))

if not (2 <= base <= 9):
    print("Основание системы счисления должно быть от 2 до 9!")
else:
    valid = all(int(digit) < base for digit in number_str)
    if valid:
        result = to_decimal(number_str, base)
        print(f"Число {number_str} в {base}-ичной системе счисления равно {result} в десятичной.")
    else:
        print("Число содержит цифры, недопустимые для данной системы счисления!")
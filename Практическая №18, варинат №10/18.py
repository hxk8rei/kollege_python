def convert_to_demical(number_str, p):
    if not (2 <= p <= 9):
        raise ValueError("Основание p должно быть от 2 до 9")
    
    result = 0
    power = 0

    for char in reversed(number_str):
        digit = int(char)
        if digit >= p:
            raise ValueError(f"Символ '{char}' недопустим для основания {p}")
        result += digit * (p ** power)
        power += 1
    return result

print(convert_to_demical("101", 2))
print(convert_to_demical("12", 3))
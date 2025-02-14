# Григорьев Максим Денисович
# По номеру дня вычислить число и месяц невисокосного года

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        day_number = int(input("Введите номер дня в году (1-365): "))
        
        if not (1 <= day_number <= 365):
            print("Ошибка! Номер дня должен быть в диапазоне от 1 до 365.")
            continue

        day_of_year = day_number
        for month, days_in_month in enumerate(days_in_months, start=1):
            if day_of_year <= days_in_month:
                print(f"Номер месяца — {month}.")
                break
            day_of_year -= days_in_month
        break

    except ValueError:
        print("Ошибка! Введите правильное числовое значение для дня.")
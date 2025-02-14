# Григорьев Максим Денисович
# В N колхозах выращивают некоторые сельскохозяйственные культуры из имеющегося перечня. Определить культуры, выращиваемые во всех колхозах, и культуры, выращиваемые только в некоторых из них.

while True:
    try:
        N = int(input("Введите количество колхозов (N): "))
        
        if N <= 0:
            print("Ошибка! Количество колхозов должно быть положительным числом.")
            continue

        cultures_all = []
        for i in range(N):
            cultures = input(f"Введите культуры для колхоза {i+1} через запятую: ").strip().split(", ")
            cultures_all.append(set(cultures))

        cultures_common = set.intersection(*cultures_all)
        print("Культуры, выращиваемые во всех колхозах:", cultures_common)

        cultures_some = set()
        for cultures in cultures_all:
            cultures_some |= cultures
        cultures_some -= cultures_common
        print("Культуры, выращиваемые только в некоторых колхозах:", cultures_some)

        break
    except ValueError:
        print("Ошибка! Введите корректное число колхозов.")

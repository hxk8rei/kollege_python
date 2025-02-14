# Григорьев Максим Денисович
# Упорядочить заданный массив английских слов по алфавиту.

while True:
    input_words = input("Введите список слов через пробел: ").strip()
    
    if not input_words:
        print("Ошибка! Список слов не должен быть пустым.")
        continue
    
    words_list = input_words.split()
    
    if any(not word.isalpha() for word in words_list):
        print("Ошибка! Все элементы должны быть английскими словами (состоящими только из букв).")
        continue

    sorted_words = sorted(words_list)
    print("Упорядоченные слова:", sorted_words)
    break
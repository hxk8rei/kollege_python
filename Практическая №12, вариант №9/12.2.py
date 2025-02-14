# Григорьев Максим Денисович
# Дан текст на русском языке. Напечатать в алфавитном порядке все звонкие согласные буквы, входящие в каждое нечетное слово и не входящие ни в одно четное слово этого текста.

while True:
    text = input("Введите текст на русском языке: ").strip()
    
    if not text:
        print("Ошибка! Текст не должен быть пустым.")
        continue

    voiced_consonants = set("бвгдеёжзийклмнпрстфхцчшщ")
    
    words = text.split()
    
    odd_words = words[::2]
    even_words = words[1::2]
    
    voiced_odd = set()
    for word in odd_words:
        voiced_odd.update([ch.lower() for ch in word if ch.lower() in voiced_consonants])
    
    voiced_even = set()
    for word in even_words:
        voiced_even.update([ch.lower() for ch in word if ch.lower() in voiced_consonants])
    
    result = voiced_odd - voiced_even
    sorted_result = sorted(result)
    
    print("Задание 2: Звонкие согласные в нечетных словах, не встречающиеся в четных:", "".join(sorted_result))
    break
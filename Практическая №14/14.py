with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Это    текст   с  лишними     пробелами")

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    cleaned_text = ' '.join(word for word in text.split() if word)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(cleaned_text)

with open('output.txt', 'r', encoding='utf-8') as f:
    print("Текст после обработки:", f.read())
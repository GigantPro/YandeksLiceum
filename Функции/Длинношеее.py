def print_long_words(text):
    text = text.lower()
    for i in text:
        if i not in ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя\
                      abcdefghijklmnopqrstuvwxyz':
            text = text.replace(i, ' ')
    a = text.split()
    for i in a:
        k = 0
        for j in i:
            if j in 'аоэиуыеёюяaeiouy':
                k += 1
        if k > 3:
            print(i)

translated_text = ''
 
 
def translate(text):
    global translated_text
    mass = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-']
    for i in range(len(text) - 1):
        if mass.count(text[i]) == 0:
            translated_text = translated_text + text[i]
    translated_text = ' '.join(translated_text.split())
    return translated_text

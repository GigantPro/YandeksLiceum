name = None


def polite_input(a):
    global name
    if not name:
        name = input('Как вас зовут?\n')
    return input(f'{name}, {a}\n')

def print_document(n):
    for i in n:
        if 'Секретно' == i[:8]:
            print('Дальнейшие материалы засекречены')
            exit()
        else:
            print(i)
    print('Напечатано без купюр')

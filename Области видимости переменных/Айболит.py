base = []
 
 
def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')
 
 
def search_card(name):
    global base
    if name not in base:
        print('Ваша карта не найдена')
    else:
        print(f'Ваша карта с номером {base.index(name) + 1} найдена')

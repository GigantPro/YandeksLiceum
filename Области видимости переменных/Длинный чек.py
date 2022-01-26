ls = []
count = 1


def add_item(name: str, price: int):
    global ls
    a = []
    a.append(name)
    a.append(price)
    a.append(1)
    ls.append(a)

        
def print_receipt():
    global count, ls
    if ls:
        summ = 0
        vsego = len(ls)
        print(f'Чек {count}. Всего предметов: {vsego}')
        count += 1
        for i in ls:
            print(f'{i[0]} - {i[1]}')
            summ += i[1]
        ls.clear()
        print(f'Итого: {summ}\n-----')


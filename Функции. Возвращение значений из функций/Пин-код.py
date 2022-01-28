def check_pin(pin):
    pin = pin.split('-')
    a = int(pin[0])
    b = int(pin[1])
    c = int(pin[2])
    if pr(a) and pl(b) and st(c):
        return 'Корректен'
    else:
        return 'Некорректен'


def pr(a):
    k = 0
    for i in range(1, a + 1):
        if a % i == 0:
            k += 1
    if k == 2:
        return True


def pl(b):
    if str(b) == str(b)[::-1]:
        return True


def st(c):
    i = 1
    while i < c:
        i *= 2
    if i == c:
        return True

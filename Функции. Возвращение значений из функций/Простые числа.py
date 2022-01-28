def prime(num):
    n = 0
    for i in range(1, num + 1):
        if num % i == 0:
            n += 1
    if n == 2:
        return 'Простое число'
    else:
        return 'Составное число'{\rtf1}

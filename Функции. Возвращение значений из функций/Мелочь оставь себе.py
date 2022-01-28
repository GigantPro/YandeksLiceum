def take_large_banknotes(n):
    a = []
    for i in n:
        if i > 10:
            a.append(i)
    return a

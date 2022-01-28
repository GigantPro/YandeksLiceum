def average(n):
    if n:
        a = sum(n) / len(n)
        if a % 1 == 0:
            return int(a)
        return a
    return 0

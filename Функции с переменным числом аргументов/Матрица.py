def matrix(n=1, m=0, a=0):
    if n == 1 and not m:
        m = 1
    elif n != 1 and not m:
        m = n
    return [[a for _ in range(m)] for _ in range(n)]

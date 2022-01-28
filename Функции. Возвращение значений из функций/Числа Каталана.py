def catalan(a):
    x = [0] * (a + 1)
    x[0] = 1
    for i in range(1, a + 1):
        for j in range(i):
            x[i] += x[j] * x[i - j - 1]
    return x[a]

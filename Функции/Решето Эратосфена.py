def eratosthenes(N):
    m = [i for i in range(N + 1)]
    m[1] = 0
    m1 = []
    if N < 4:
        return
    for i in range(2, N + 1):
        for j in range(i * 2, N + 1, i):
            if m[j] != 0:
                m[j] = 0
                m1.append(j)
    print(" ".join(str(x) for x in m1))

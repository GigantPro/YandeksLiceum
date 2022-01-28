def find_mountain(n):
    x, y = 0, 0
    for i in range(len(n)):
        for j in range(len(n[0])):
            if int(n[x][y]) < int(n[i][j]):
                x, y = i, j
    return x, y

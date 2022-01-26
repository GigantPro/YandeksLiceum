def transpose(m):
    arr = []
    for i in range(len(m[0])):
        temp = []
        for j in range(len(m)):
            temp.append(m[j][i])
        arr.append(temp)
    m.clear()
    m.extend(arr)

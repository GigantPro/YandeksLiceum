def find_farthest_orbit(ls):
    for i in ls:
        if i[0] == i[1]:
            ls.remove(i)
        else:
            continue
    lenn = list(map(lambda x: x[0] * x[1] * 3.14, ls))
    return ls[lenn.index(max(lenn))]
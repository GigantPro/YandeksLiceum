def t2c(f):
    a = f[:1]
    b = f[1:]
    r = int(b)
    c = 'ABCDEFGH'.find(a) + 1
    return (c, r)


def c2t(k):
    (c, r) = k
    return 'ABCDEFGH'[c - 1] + str(r)


def possible_turns(f):
    (c, r) = t2c(f)
    tmp = []
    tmp.append((c + 2, r + 1))
    tmp.append((c + 2, r - 1))
    tmp.append((c - 2, r + 1))
    tmp.append((c - 2, r - 1))
    tmp.append((c + 1, r + 2))
    tmp.append((c - 1, r + 2))
    tmp.append((c + 1, r - 2))
    tmp.append((c - 1, r - 2))
    res = []
    for ((a, b)) in tmp:
        if (a > 0) & (b > 0) & (a <= 8) & (b <= 8):
            res += [c2t((a, b))]
    return sorted(res)

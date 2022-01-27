def squared(a, b, c):
    count = 0
    for i in range(a, b + 1):
        if (i ** 2) % c != 0:
            x = str(i ** 2)
            print(f"{x:<4}", end=' ')
        count += 1
        if count == 10:
            print()
            count = 0

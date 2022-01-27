def golden_ratio(i):
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    j = abs(len(fib) - i)
    for k in range(i):
        if i > len(fib):
            for gg in range(j + 1):
                fib.append(fib[-2] + fib[-1])
    print(fib[i] / fib[i - 1])

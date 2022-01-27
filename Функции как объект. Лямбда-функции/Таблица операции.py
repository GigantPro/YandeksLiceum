def print_operation_table(func, count=9, count2=9):
    for i in range(1, count + 1):
        for j in range(1, count2 + 1):
            if j == 9:
                print(func(i, j))
            else:
                print(func(i, j), end='\t')
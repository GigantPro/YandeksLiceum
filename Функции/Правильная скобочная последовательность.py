def bracket_check(a):
    mass = []
    flag = False
    for i in range(len(a)):
        if a[i] == '(':
            mass.append(a[i])
        elif a[i] == ')' and len(mass) == 0:
            flag = True
            break
        elif a[i] == ')' and mass[-1] == '(':
            del mass[-1]
    if len(mass) == 0 and not flag:
        print('YES')
    else:
        print('NO')

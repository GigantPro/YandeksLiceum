def line(a, q):
    k = float(a.split('x')[0])
    b = float(a.split('x')[1])
    x = float(q.split(';')[0])
    y = float(q.split(';')[1])
    if y == k * x + b:
        print('True')
    else:
        print('False')

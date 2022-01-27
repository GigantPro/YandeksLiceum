summ = 0
a = filter(lambda x: x % 9 == 0, range(10, 100))
b = map(lambda x: x * x, a)
summ = sum(b)
print(summ)

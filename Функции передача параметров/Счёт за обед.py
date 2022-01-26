def count_food(a):
    summ = 0
    for i in a:
        summ += daily_food[i - 1]
    return summ

def quarter(xcoord, ycoord):
    num = ''
    if xcoord > 0 and ycoord > 0:
        num = 'I'
    elif xcoord < 0 and ycoord > 0:
        num = 'II'
    elif xcoord < 0 and ycoord < 0:
        num = 'III'
    else:
        num = 'IV'
    print(num, 'четверть')

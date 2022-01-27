def lucky(ticket):
    global lastTicket
    x, y = int(len(str(ticket)) / 2), int(len(str(lastTicket)) / 2)
    a, b = [int(i) for i in str(ticket)[x:]], [int(i) for i in str(ticket)[:x]]
    c, d = [int(i) for i in str(lastTicket)[:y]], [int(i) for i in str(lastTicket)[y:]]
    if sum(a, 0) == sum(b, 0) and sum(c, 0) == sum(d, 0):
        return 'Счастливый'
    else:
        return 'Несчастливый'

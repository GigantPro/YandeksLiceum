def password_level(pas):
    digit_ = digit(pas)
    upp = up(pas)
    down = dow(pas)
    if len(pas) >= 6:
        if (digit_ and not(upp) and not(down)) or\
           (not(digit_) and (upp) and not(down)) or\
           (not(digit_) and not(upp) and (down)):
            return 'Ненадежный пароль'
        elif upp and down and digit_:
            return 'Надежный пароль'
        elif (upp and down) or (upp and digit_) or (down and digit_):
            return 'Слабый пароль'
    else:
        return 'Недопустимый пароль'


def digit(a):
    x = False
    for i in a:
        if i.isdigit():
            x = True
    if x:
        return True
    else:
        return False


def up(a):
    x = False
    for i in a:
        if i.isalpha() and i.isupper():
            x = True
    if x:
        return True
    else:
        return False


def dow(a):
    x = False
    for i in a:
        if i.isalpha() and i.islower():
            x = True
    if x:
        return True
    else:
        return False 

def roots_of_quadratic_equation(a, b, c):
    d = (b ** 2 - (4 * a * c))
    if a == b == c == 0:
        m = ['all']
        return m
    elif a == 0 and b != 0:
        m = [(-c / b)]
        return m
    elif a == b == 0:
        m = []
        return m
    elif d == 0:
        m = [(-b + d ** 0.5) // (2 * a)]
        return m
    elif d < 0:
        m = []
        return m
    else:
        m = [(-b + d ** 0.5) // (2 * a), (-b - d ** 0.5) // (2 * a)]
        return m

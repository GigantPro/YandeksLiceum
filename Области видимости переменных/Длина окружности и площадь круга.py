pi = 3.14159


def circle_length(r):
    return 2 * pi * r


def circle_area(r):
    return pi * (r**2)


def main():
    r = float(input())
    print(circle_length(r), circle_area(r))

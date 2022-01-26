def smaller_root(p, q):
    return min([(-p + ((p**2) - 4 * q)**0.5) / 2, (-p - ((p**2) - 4 * q)**0.5) / 2])


def larger_root(p, q):
    return max([(-p + ((p**2) - 4 * q)**0.5) / 2, (-p - ((p**2) - 4 * q)**0.5) / 2])


def discriminant(a, b, c):
    return b**2 - (4 * a * c)


def main():
    b, c = float(input()), float(input())
    print(discriminant(1, b, c))
    print(smaller_root(b, c), larger_root(b, c))

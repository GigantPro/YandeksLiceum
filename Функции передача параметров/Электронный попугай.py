arr = []


def parrot(phrase):
    if phrase in arr:
        print(phrase)
    else:
        arr.append(phrase)

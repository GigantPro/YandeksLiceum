ls = []


def print_only_new(message):
    if message not in ls:
        print(message)
    ls.append(message)

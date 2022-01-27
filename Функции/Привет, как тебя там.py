def who_are_you_and_hello():
    a = input()
    while not(a.capitalize() == a and a.isalpha()):
        a = input()
    print(f'Привет, {a}!')

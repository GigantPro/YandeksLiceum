def palindrome(a):
    a = a.lower()
    if ''.join(a.split())[::-1] == ''.join(a.split()):
        return ('Палиндром')
    else:
        return ('Не палиндром')

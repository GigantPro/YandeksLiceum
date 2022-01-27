def ask_password(login, password, success, failure):
    glas = 'aeiouy'
    count_glas = 0
    sogl_log = ''
    sogl_pas = ''
    flag1 = False
    flag2 = False
    for i in password:
        if i not in glas:
            sogl_pas += i
    for i in login:
        if i not in glas:
            sogl_log += i
    if sogl_log != sogl_pas:
        flag1 = True
    for i in password:
        if i in glas:
            count_glas += 1
    if count_glas != 3:
        flag2 = True
    if flag1 and not flag2:
        err = 'Wrong consonants'.upper()
        failure(login, err)
    elif flag2 and not flag1:
        err = 'Wrong number of vowels'.upper()
        failure(login, err)
    elif flag1 and flag2:
        err = 'Everything is wrong'.upper()
        failure(login, err)
    else:
        success(login)


def main(login, password):
    ask_password(login, password, lambda login: print(f'Привет, {login.lower()}!'), lambda login, err: print(f'Кто-то пытался притвориться пользователем {login.lower()}, но в пароле допустил ошибку: {err}.'))
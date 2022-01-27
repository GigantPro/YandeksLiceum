horses = []


def do_bet(horse, bet):
    if bet == 0 or horse in horses or horse > 10 or horse <= 0:
        print('Что-то пошло не так, попробуйте еще раз')
        return
    else:
        print('Ваша ставка в размере', bet, 'на лошадь', horse, 'принята')
        horses.append(horse)
        return
 
 

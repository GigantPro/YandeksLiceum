g = []
d = ''
f = dict()
 
 
def print_application_for_leave():
    print(f'Заявление на отпуск в период {f[d]}.', end=' ')
    print(*g)
 
 
def print_holiday_money_claim(amount):
    print(f'Прошу выплатить {amount} отпускных денег.', end=' ')
    print(*g)
 
 
def print_attorney_letter(to_whom):
    print(f'На время отпуска в период {f[d]} моим заместителем назначается {to_whom}.', end=' ')
    print(*g)
 
 
def setup_profile(name, vacation_dates):
    global f
    global d
    global g
    f = dict()
    d = name
    f[name] = vacation_dates
    g = list(f.keys())
 

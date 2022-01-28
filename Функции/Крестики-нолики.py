def tic_tac_toe(field):
    if (field[0][0] == field[0][1] == field[0][2] == 'x') or \
            (field[1][0] == field[1][1] == field[1][2] == 'x') or \
            (field[0][0] == field[2][1] == field[2][2] == 'x') or \
            (field[0][0] == field[1][1] == field[2][2] == 'x') or \
            (field[0][2] == field[1][1] == field[2][0] == 'x') or \
            (field[0][0] == field[1][0] == field[2][0] == 'x') or \
            (field[0][1] == field[1][1] == field[2][1] == 'x') or \
            (field[0][2] == field[1][2] == field[2][2] == 'x'):
        print('x win')
    elif (field[0][0] == field[0][1] == field[0][2] == '0') or \
            (field[1][0] == field[1][1] == field[1][2] == '0') or \
            (field[2][0] == field[2][1] == field[2][2] == '0') or \
            (field[0][0] == field[1][1] == field[2][2] == '0') or \
            (field[0][2] == field[1][1] == field[2][0] == '0') or \
            (field[0][0] == field[1][0] == field[2][0] == '0') or \
            (field[0][1] == field[1][1] == field[2][1] == '0') or \
            (field[0][2] == field[1][2] == field[2][2] == '0'):
        print('0 win')
    else:
        print('draw')

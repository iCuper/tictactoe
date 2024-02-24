tab = []
tab2 = []
tab3 = {'00': '1', '01': '2', '02': '3', '10': '4', '11': '5', '12': '6', '20': '7', '21': '8', '22': '9'}
win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
type_board = 2
type_uprav = 2


def clean_tab():
    global tab
    global tab2
    tab = list(range(1, 10))
    tab2 = list('-' * 9)


def cls():
    print('\n' * 50)


def check_win():
    for i in win:
        if tab[i[0]] == tab[i[1]] == tab[i[2]]:
            return tab[i[0]]
    return False


def write_pole(board):
    cls()
    if board == 1:
        print('  0 1 2')
        chet = 0
        for i in range(0, 9, 3):
            print(chet, *tab2[i:i + 3])
            chet += 1

    if board == 2:
        for i in range(0, 9, 3):
            print(*tab[i:i + 3])
    print('\n')


def move_player(xo, uprav):
    if uprav == 2:
        while True:
            posic = int(input('Куда поставить ' + xo + '?: '))
            if 1 <= posic <= 9:
                posic = int(posic) - 1
                if tab[int(posic)] != 'X' and tab[int(posic)] != 'O':
                    return posic
                else:
                    print('Клетка уже занята! Повторите еще раз!')
            else:
                print('Ошибка! Попробуйте еще раз.')
    if uprav == 1:
        while True:
            posic = input('Куда поставить ' + xo + '?: ')
            if tab3.get(posic):
                posic = int(tab3.get(posic)) - 1
                if tab[posic] != 'X' and tab[posic] != 'O':
                    return posic
                else:
                    print('Клетка уже занята! Повторите еще раз!')
            else:
                print('Ошибка! Попробуйте еще раз.\nКоординаты должны быть следущего вида "02" где 0 - строка, '
                      'где 2 - столбец')


def start_game():
    write_pole(type_board)
    move = 0
    while True:
        if move > 8:
            print('Ничья!\nПовторить еще раз?\n1.Да\n2.Нет (выйти в главное меню)\n')
            choise = int(input('Выбор:'))
            if choise == 1:
                clean_tab()
                start_game()
            else:
                menu()
        if move % 2 == 0:
            move += 1
            pos = int(move_player('X', type_uprav))
            tab[pos] = 'X'
            tab2[pos] = 'X'
            write_pole(type_board)
        else:
            move += 1
            pos = int(move_player('O', type_uprav))
            tab[pos] = 'O'
            tab2[pos] = 'O'
            write_pole(type_board)
        if check_win():
            print(check_win(), ' Выиграл!')
            print('\nПовторить еще раз?\n1.Да\n2.Нет (выйти в главное меню)\n')
            choise = int(input('Выбор:'))
            if choise == 1:
                clean_tab()
                start_game()
            else:
                menu()


def menu():
    cls()
    clean_tab()
    print('\t\t\nКРЕСТИКИ НОЛИКИ\n\n')
    print('[1] Начать игру\n[2] Настройки\n[3] Помощь\n[4] Об игре\n[5] Выход\n')
    choise = int(input('Выбор:'))
    if choise == 1:
        start_game()
    if choise == 2:
        print('\nВыберите вид доски:')
        chet = 0
        print('  0 1 2')
        for i in range(0, 9, 3):
            print(chet, '- - -\t\t\t\t', *tab[i:i + 3])
            chet += 1
        print('[1] Вид № 1\t\t\t [2] Вид № 2 (по умолчанию) \n')
        global type_board
        type_board = int(input('Выбор:'))
        if type_board != 1:
            type_board = 2
        print('\nВыберите тип управления:')
        chet = 0
        print('  0 1 2')
        for i in range(0, 9, 3):
            print(chet, '\t' * 7, *tab[i:i + 3])
            chet += 1
        print(' [1] По координатам\t\t\t[2] По номеру ячейки (по умолчанию)\n(читать помощь)\n')
        global type_uprav
        type_uprav = int(input('Выбор:'))
        if type_uprav != 1:
            type_uprav = 2
        menu()
    if choise == 3:
        cls()
        print('\t\t\t\tПравила игры\n\tИгроки по очереди ставят на свободные клетки поля 3×3 знаки\n'
              '(один всегда крестики, другой всегда нолики).\nПервый, выстроивший в ряд 3 своих фигуры'
              ' по вертикали, горизонтали или большой диагонали, выигрывает.\n\nУправление по координатам прозводится'
              ' путем ввода координат в формате "01"\n\t\t\tГде "0" - строка поля, а "1" - столбец поля\n'
              'Управление по номерам ячеек производится путем выбора номера ячейки от 1 до 9')
        input('\nНажмите на "Enter" чтобы выйти в меню...')
        menu()
    if choise == 4:
        cls()
        print('\nИгра была создана в рамках образовательного курса SkillFactory')
        print('\n\n\t\tАвтор: Шарип Хаджаров\n')
        input('\nНажмите на "Enter" чтобы выйти в меню...')
        menu()
    if choise == 5:
        quit()
    else:
        print('Ошибка повторите еще раз!')
        menu()


menu()

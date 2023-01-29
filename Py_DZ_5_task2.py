# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

#  1 | 2 | X
#  4 | X | O
#  X | 8 | O

def matrix(mtr): # Отрисовка таблицы

    print('\n')
    print('\t    |    |    ')
    print('\t  {} |  {} |  {} '.format(mtr[0], mtr[1], mtr[2]))
    print('\t____|____|____')

    print('\t    |    |    ')
    print('\t  {} |  {} |  {}  '.format(mtr[3], mtr[4], mtr[5]))
    print('\t____|____|____')

    print('\t    |    |    ')
    print('\t  {} |  {} |  {}  '.format(mtr[6], mtr[7], mtr[8]))
    print('\t    |    |    ')
print('\n')

mtr = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Список ячеек
step_count = 0                    # Счетчик ходов
win_status = False                # Статус выгирыша
win_lst = '123_456_789_147_258_369_159_357'  # Строка выигрышных комбинаций
p = int(input(f'Если игру начинает X, то введите цифру: 1\nЕсли игру начинает O, то введите цифру: 0\n '))
while not win_status:  # Пока никто не выграл
    matrix(mtr)        #  Отрисовка таблицы
    if p == 1: p = 0   #  Переход хода
    else:
        p = 1
    if step_count == 9:  # Все ячейки заняты, но никто не выиграл
        print('НИЧЬЯ')
        break
    step_count += 1      # Счетчик ходов + ход
    if p == 0:
        point = int(input(f'Ход игрока X - выбирете номер ячейки \n '))    
        if point not in mtr:  # Если в списке нет номера ячейки - воврат к выбру
            print(f'Место занято - выбирете свободный номер \n ') #
            continue
        win_lst = win_lst.replace(str(point), 'X') # Иначе заменяем в строке выигрышных комбинаций число на символ игрока      
        for x in range(9):  # В списке ячеек меняем номер ячейки на символ игрока (выбрать его будет невозможно)
            if mtr[x] == point: mtr[x] = 'X'
        if 'XXX' in win_lst:  # Если в строке выигрышных комбинаций есть ХХХ, то называем победителя и прерываем выполнение программы  
            print('ИГРОК X ВЫИГРАЛ!')
            break

    if p == 1:  # Те же операции для втрого игрока 
        point = int(input(f'Ход игрока 0 - выбирете номер ячейки \n '))
        if point not in mtr:
            print(f'Место занято - выбирете свободный номер \n ')
            continue
        win_lst = win_lst.replace(str(point), '0')
        for x in range(9): 
            if mtr[x] == point: mtr[x] = '0'
        if '000' in win_lst:
            print('ИГРОК 0 ВЫИГРАЛ!')
            break
exit() #


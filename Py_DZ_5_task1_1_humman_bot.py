#  ЧЕЛОВЕК ПРОТИВ КОМПЬЮТЕРА

from random import randint
x0 = int(60)
step = 0
p = randint(1, 2)
if p == 1:
    print('Игру начинает ЧЕЛОВЕК')
if p == 2:
    print('Игру начинает КОМПЬЮТЕР')

while x0 > 0:        
        if p == 1 and x0 > 0:        
            p = 2
            step = int(input(f'Введите количество конфет от 1 до 28, которое хотите забрать за один ход: - '))
            if step < 1 or step > 28:
                print(f'Вы нажали {step}, жульничаете!\nВводите числа по правилам  от 1 до 28')
                break
            x0 -= step
            print(f'ЧЕЛОВЕК забрал {step} конфет, осталось {x0} \n\nХод  КОМПЬЮТЕРА\n')            
        else:
            if x0 > 0: 
                p = 1
                step = randint(1, 28)
                x0 -= step
                print(f'КОМПЬЮТЕР забрал {step} конфет, осталось {x0} \n\nХод  ЧЕЛОВЕКА\n')                   
if p == 2:
    print(f'Конфет не осталось - ЧЕЛОВЕК ПОБЕДИЛ!')    
if p == 1:
    print(f'Конфет не осталось - КОМПЬЮТЕР ПОБЕДИЛ!')
exit()    
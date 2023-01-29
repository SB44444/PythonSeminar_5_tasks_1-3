#  3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные данные хранятся в отдельных текстовых файлах.
    #  RLE Kодер
def encode(cod_str):
    out_str = ""
    count = 1
    char = cod_str[0]
    for i in range(1, len(cod_str)):  # Цикл по индексам строки
        if cod_str[i] == char:        # Считаем к-во одинаковых символов
            count += 1
        else:
            out_str += str(count) + char  # Если символ изменился, дбваляем его строковое к-во повторений
            char = cod_str[i]
            count = 1
    else:    
        out_str += str(count) + char  # Если символ не повторился, дбваляем его с 1
    return out_str
	#  RLE Декодер
def decode(out_str):  
    str = ''
    count = ''
    for i in out_str:  # Для каждого элемента в строке 
        if i.isdigit():  # Если символ число - добавляем в строку числового значения 
            count += i              
        else:
            str = str + int(count)*i  # Если символ, умножаем на коэфф. приведенный к числу
            count = '' # Облуляем строку числового коэффициента 
    return str
print('Чтобы выполнить кодирование нажмите клавишу c') # Выбор действия, чтение изапись файлов
print('Чтобы выполнить кодирование нажмите клавишу d')
state = input()
if state == "c":
    with open('origin_file.TXT', 'r') as f:
        cod_str = f.read()
    with open('coded_file.txt', 'w') as f:
        out_str = encode(cod_str)
        f.write(out_str)
    print('Исходные данные:    ' + cod_str)
    print('Сжатые данные:    ' + out_str)
elif state == 'd':
    with open('coded_file.txt', 'r') as f:
        cod_str = f.read()
    with open('decoded_file.txt', 'w') as f:
        out_str = decode(cod_str)
        f.write(out_str)
    print('Сжатые данные:         ' + cod_str)
    print('Раскодированные данные:  ' + out_str)    
else:
    print('Нажмите клавишу c или d')        

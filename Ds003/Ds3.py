# Задача 3. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

try:
    from random import randint

    def create_list(k):
        list = []
        for i in range(k + 1):
            list.append(randint(0, 100)) 
        return list
        
    def create_str_сoef(list):
        st = ''
        for i in range(len(list)):
            if i < len(list) - 2 and list[i] != 0:
                st += str(list[i]) + 'x^' + str(len(list) - i - 1) + ' + '
                
            elif i == len(list) - 2 and list[i] != 0:
                st += str(list[i]) + 'x + '

            elif i == len(list) - 1:
                st += str(list[i]) + ' = 0'
        return st

    def write_file(st):
        with open('Ds003/Ds3t.txt', 'w') as data:
            data.write(st)

    def print_result():
        k = int(input('Введите натуральную степень k: '))
        if k < 1:
            print('!! Введите натуральное число !!')
            return
        list = create_list(k)
        print('Результат формирования списка:')
        print(list)
        print(f'Результат формирования многочлена степени k({k}):')
        print(create_str_сoef(list))
        write_file(create_str_сoef(list))
        
    print_result()
except:
    print('!! Введите натуральное число !!')
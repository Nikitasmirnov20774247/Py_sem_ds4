# Задача 2. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

try:
    def create_list(size):
        list = []
        for i in range(size):
            list.append(str(input('Введите число: ')))
        return list

    def original_num(list):
        list2 = []
        for i in list:
            if i not in list2:
                list2.append(i)
        return list2

    def print_list():
        size = int(input('Введите размер списка: '))
        list = create_list(size)
        list2 = original_num(list)
        print('Результат формирования списка:')
        print(list)
        print(f'Список из неповторяющихся элементов: {list2}')

    print_list()
except:
    print ('!! Введите целое число !!')
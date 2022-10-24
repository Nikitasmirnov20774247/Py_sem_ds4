# Задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

try:
    def primfacs(n):
        i = 2
        list = []
        while i * i <= n:
            if n % i == 0:
                list.append(i)
                n//=i
            else:
                i += 1
        list.append(n)
        return list

    def print_result():
        n = int(input("Введите натуральное число: "))
        if n < 1:
                print('!! Введите натуральное число !!')
                return
        result = primfacs(n)
        print(f"Результат формирования простых множителей числа {n}: {result}")

    print_result()
except:
    print('!! Введите натуральное число !!')
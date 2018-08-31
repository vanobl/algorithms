#Определить, какое число в массиве встречается чаще всего

import random

repeat = {}

#определим пустой список
chisla_list = [1, 2, 3, 5, 6, 5, 2, 5, 2, 1]
for i in chisla_list:
    if any(repeat):
        if chisla_list.count(i) > int(list(repeat.values())[0]):
            repeat.clear()
            repeat.update({i: chisla_list.count(i)})
        elif chisla_list.count(i) == int(list(repeat.values())[0]):
            repeat.update({i: chisla_list.count(i)})
    else:
        repeat.update({i: chisla_list.count(i)})

#выводим результат
for i, z in repeat.items():
    print(f'Число: {i} повторяется: {z} раз(а).')
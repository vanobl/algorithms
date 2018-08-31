#В одномерном массиве найти сумму элементов, находящихся между 
# минимальным и максимальным элементами. Сами минимальный и 
# максимальный элементы в сумму не включать.

import random

#определим пустой список
chisla_list = []

min_chislo = {}
max_chislo = {}

#заполним список случайными числами
for i in range(10):
    a = random.randint(-100, 100)
    chisla_list.append(a)
print(chisla_list)

#узнаем минисмальное число
for i, x in enumerate(chisla_list):
    loc_min_chislo = min_chislo.copy()
    if any(loc_min_chislo):
        for k, y in loc_min_chislo.items():
            if x < y:
                min_chislo.clear()
                min_chislo.update({i: x})
    else:
        min_chislo.update({i: x})

#узнаём максимальное число
for i, x in enumerate(chisla_list):
    loc_max_chislo = max_chislo.copy()
    if any(loc_max_chislo):
        for k, y in loc_max_chislo.items():
            if x > y:
                max_chislo.clear()
                max_chislo.update({i: x})
    else:
        max_chislo.update({i: x})

print(f'минимальное число: {min_chislo}')
print(f'максимальное число: {max_chislo}')

summ = 0

if int(list(max_chislo.keys())[0]) < int(list(min_chislo.keys())[0]):
    for i in range(int(list(max_chislo.keys())[0]) + 1, int(list(min_chislo.keys())[0])):
        summ += chisla_list[i]
else:
    for i in range(int(list(min_chislo.keys())[0]) + 1, int(list(max_chislo.keys())[0])):
        summ += chisla_list[i]

print(summ)
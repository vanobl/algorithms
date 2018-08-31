#В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), 
# так и различаться.

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

#узнаём предминимальное число
for i, x in enumerate(chisla_list):
    loc_max_chislo = max_chislo.copy()
    if any(loc_max_chislo):
        for k, y in loc_max_chislo.items():
            if int(list(min_chislo.values())[0]) == x and int(list(min_chislo.keys())[0]) == i:
                pass
            else:
                if x < y:
                    max_chislo.clear()
                    max_chislo.update({i: x})
    else:
        max_chislo.update({i: x})

print(f'минимальное число: {min_chislo}')
print(f'предминимальное число: {max_chislo}')
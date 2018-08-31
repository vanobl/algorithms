#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

#удаляем минимальное значение
chisla_list.pop(int(list(min_chislo.keys())[0]))

#удаляем максимальное число
if int(list(max_chislo.keys())[0]) < int(list(min_chislo.keys())[0]):
    chisla_list.pop(int(list(max_chislo.keys())[0]))
else:
    chisla_list.pop(int(list(max_chislo.keys())[0]) - 1)

print(chisla_list)

#print(list(min_chislo.values())[0])

if int(list(max_chislo.keys())[0]) < int(list(min_chislo.keys())[0]):
    #вставляем минимальное число
    chisla_list.insert(int(list(max_chislo.keys())[0]), list(min_chislo.values())[0])

    #вставляем максимальное число
    chisla_list.insert(int(list(min_chislo.keys())[0]), list(max_chislo.values())[0])
else:
    #вставляем максимальное число
    chisla_list.insert(int(list(min_chislo.keys())[0]), list(max_chislo.values())[0])

    #вставляем минимальное число
    chisla_list.insert(int(list(max_chislo.keys())[0]), list(min_chislo.values())[0])

print(chisla_list)
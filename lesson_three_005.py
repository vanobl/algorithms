#В массиве найти максимальный отрицательный элемент. Вывести на экран 
# его значение и позицию в массиве.

import random

#определим пустой список
chisla_list = []

max_chislo = {}

#заполним список случайными числами
for i in range(10):
    a = random.randint(-100, 100)
    chisla_list.append(a)
print(chisla_list)

#узнаём максимальное число
for i, x in enumerate(chisla_list):
    if not any(max_chislo):
        if x < 0:
            max_chislo.update({i: x})
    else:
        if int(list(max_chislo.values())[0]) < x and x < 0:
            max_chislo.clear()
            max_chislo.update({i: x})

print(f'Максимальное отрицательное число {list(max_chislo.values())[0]}')
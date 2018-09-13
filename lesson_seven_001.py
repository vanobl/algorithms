# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100]. Вывести на экран 
# исходный и отсортированный массивы.

import random

# определим массив для заполнения
int_list = []

# заполним массив
for i in range(10):
    int_list.append(random.randint(-100, 100))

n = 1

# выведем заполненный массив
print(f'Массив заполнен: {int_list}')

while n < len(int_list):
    for i in range(len(int_list) - n):
        if int_list[i] > int_list[i + 1]:
            int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]
        print(int_list)
    n += 1

# print(int_list)
# print(min(int_list))
# print(max(int_list))
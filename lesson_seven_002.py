# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный 
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def my_sort(mylist):
    # определим массив для заполнения
    int_list = mylist

    # заполним массив
    for i in range(10):
        int_list.append(random.randint(-100, 100))
        
    print(mylist)

my_list = []

my_sort(my_list)
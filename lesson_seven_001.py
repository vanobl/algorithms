#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них 
# кратны любому из чисел в диапазоне от 2 до 9.
import sys

# определим словарь для кратных чисел
kratnie = {}

# переменная для анализа
a = sys.getsizeof(kratnie)
# выведем размер пустого списка
print(f'Размер переменной "kratnie" после создания: {sys.getsizeof(kratnie)}')

# определим какие из чисел являются кратными
for i in range(2, 100):
    for y in range(2, 10):
        if i % y == 0:
            kratnie.update({i: y})

# выведем кратные числа
for i, y in kratnie.items():
    print(f'{i} кратно {y}')

# выведем размер заполненого списка
print(f'Размер переменной "kratnie" после заполнения: {sys.getsizeof(kratnie)}')

# изменение памяти
print(f'Размер занимаемой памяти переменной "kratnie" увеличился на {sys.getsizeof(kratnie) - a}')

# количество ссылок
print(f'Количество ссылок: {sys.getrefcount(kratnie)}')
#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них 
# кратны любому из чисел в диапазоне от 2 до 9.

#определим словарь для кратных чисел
kratnie = {}

#определим какие из чисел являются кратными
for i in range(2, 100):
    for y in range(2, 10):
        if i % y == 0:
            kratnie.update({i: y})

#выведем кратные числа
for i, y in kratnie.items():
    print(f'{i} кратно {y}')
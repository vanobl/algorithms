import random

print('1. int')
print('2. float')
print('3. символ от a до z')
render_req = input('Выбирите формат данных (1-3): ')

if render_req == '1':
    m1 = input('Введите диапозон в формате (x;y): ')
    x1, x2 = map(int, m1.split(';'))
    z = random.randint(x1, x2)
    print(f'Результат генерации случайного целого числа = {z}')
elif render_req == '2':
    m1 = input('Введите диапозон в формате (x;y): ')
    x1, x2 = map(float, m1.split(';'))
    z = random.uniform(x1, x2)
    print(f'Результат генерации случайного вещественного числа = {z}')
elif render_req == '3':
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    z = random.choice(allLetters)
    print(f'Результат генерации случайного символа от a до z = {z}')
else:
    print('Введено не верное значение.')

#ветка 1
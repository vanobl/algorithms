#В программе генерируется случайное целое число от 0 до 100. Пользователь 
# должен его отгадать не более чем за 10 попыток. После каждой неудачной 
# попытки должно сообщаться, больше или меньше загаданного введенное 
# пользователем число. Если за 10 попыток число не отгадано, то вывести его.

import random

#генерируем случайное число
a = random.randint(0, 100)
#print(a)

popitki = 10

while popitki > 0:
    print(f'Осталось попыток {popitki}')
    b = int(input('Введите число: '))
    if b == a:
        print(f'Вы угадали! Число {a}')
        break
    else:
        if b < a:
            print('Ваше число меньше загаданного.')
        elif b > a:
            print('Ваше число больше загаданного')
    popitki -= 1

print('Программа завершена')
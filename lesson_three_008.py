#Посчитать, сколько раз встречается определенная цифра в введенной 
# последовательности чисел. Количество вводимых чисел и цифра, которую 
# необходимо посчитать, задаются вводом с клавиатуры

kol_chisel = int(input('Сколько чисел вы хотите ввести? '))
cifra = input('Какую цифру хотите найти? ')

chisla = ''

for i in range(kol_chisel):
    chisla += input('Введите число: ')

c = chisla.count(cifra)
print(f'Искомая цифра встречается {c} раз(а).')
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

a = int(input('Введите целое число: '))
chislo = 1
summa = 0

for i in range(a):
    summa += chislo
    chislo /= 2

print(summa)
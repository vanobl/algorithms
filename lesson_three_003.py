# Сформировать из введенного числа обратное по порядку входящих в него цифр и 
# вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

chislo = input('Введите целое число: ')
chislo2 = []
dlina = len(chislo)

while dlina:
    dlina -= 1
    chislo2.append(chislo[dlina])

a = int(''.join(chislo2))

print(a)
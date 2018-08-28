#Среди натуральных чисел, которые были введены, найти наибольшее по 
# сумме цифр. Вывести на экран это число и сумму его цифр

chisla = []
max_chisla = {}
chislo = 0
max_summ = 0

while True:
    pagnanais = input('Хотите ввести число? (y/n): ')
    if pagnanais == 'y':
        chisla.append(int(input('Введите число: ')))
    elif pagnanais == 'n':
        break

for i in chisla:
    ch = i
    summ = 0
    while ch > 0:
        d = ch % 10
        ch = ch // 10
        summ += d
    if max_summ < summ:
        max_summ = summ
        max_chisla.clear()
        max_chisla.update({i: max_summ})
    elif max_summ == summ:
        max_chisla.update({i: max_summ})

    #print(f'Сумма цифр числа {i} = {summ}')
#print(max_chisla)
for i, y in max_chisla.items():
    print(f'Сумма цифр числа {i} = {y}')
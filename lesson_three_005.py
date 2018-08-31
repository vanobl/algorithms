#Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 
# 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: 
# по десять пар «код-символ» в каждой строке.

spisok = ''
chislo = 0

for i in range(78, 128):
    if chislo < 9:
        if i < 100:
            spisok += f' {i}: {chr(i)} '
            chislo += 1
        else:
            spisok += f'{i}: {chr(i)} '
            chislo += 1
    else:
        if i < 100:
            spisok += f' {i}: {chr(i)}\n'
            chislo = 0
        else:
            spisok += f'{i}: {chr(i)}\n'
            chislo = 0
print(spisok)
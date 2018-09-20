# Определение количества различных подстрок с использованием хеш-функции. 
# Пусть дана строка S длиной N. Например, состоящая только из маленьких 
# латинских букв. Требуется найти количество различных подстрок в этой 
# строке. Для решения задачи рекомендую воспользоваться алгоритмом sha1 
# из модуля hashlib или встроенной в python функцией hash()
import hashlib

my_str = 'jpmpzwweyg'
finde_sub = []
count_hash = 0

for i in range(1, len(my_str)):
    for y in range(len(my_str)):
        sub = my_str[y:y+i]
        if len(sub) >= i:
            sub_hash = hashlib.sha1(sub.encode('utf-8')).hexdigest()

            if finde_sub.count(sub_hash) == 0:
                finde_sub.append(sub_hash)
                count_hash += 1

print(f'Количество не одинаковых подстрок рyавно {count_hash}.')


answer = input('Хотите просмотреть хэш суммы всех подстрок? (y/n): ')

if answer == 'Y':
    for i in finde_sub:
        print(i)
else:
    print('Вего хорошего!')
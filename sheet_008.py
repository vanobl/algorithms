import datetime

year = int(input('Введите год в формате 1900: '))

first_date = datetime.date(year, 1, 1)
second_date = datetime.date(year, 12, 31)

find_days = second_date - first_date
days = str(find_days).split(' ')[0]

if days == '364':
    print('обычный')
else:
    print('високосный')
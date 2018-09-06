# Пользователь вводит данные о количестве предприятий, их наименования и прибыль 
# за 4 квартала для каждого предприятия. Программа должна определить среднюю 
# прибыль (за год для всех предприятий) и вывести наименования предприятий, 
# чья прибыль выше среднего и отдельно вывести наименования предприятий, 
# чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

quantity_company = int(input('Введите количество предприятий, которое хотите внести в стат. отчёт: '))
name_company = []
profit_companis = []
full_summ = 0
average_value_companys = []

# попросим пользователя ввести названия предприятий
for i in range(quantity_company):
    name_company.append(input(f'Введите название компании {i + 1}: '))

# попросим пользователя ввести прибыль для каждого предприятия поквартально.
for i in range(quantity_company):
    profit_company = []
    for y in range(4):
        profit_company.append(float(input(f'Введите прибыль {name_company[i]} за {y + 1 } квартал: ')))

    profit_companis.append(profit_company)

# определим среднее значение прибыли всех предприятий
for i in profit_companis:
    value = 0
    for y in i:
        full_summ += y
        value += y
    average_value_companys.append(round(value / 4))

# подсчитаем среднее значение и запомним его
average_value = round((full_summ / (quantity_company * 4)), 2)

for i in range(quantity_company):
    if average_value_companys[i] > average_value:
        print(f'Компания {name_company[i]} получила среднюю прибыль {average_value_companys[i]} больше среднего значения {average_value}')
    elif average_value_companys[i] < average_value:
        print(f'Компания {name_company[i]} получила среднюю прибыль {average_value_companys[i]} меньше среднего значения {average_value}')
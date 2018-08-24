# По введенным пользователем координатам двух точек вывести уравнение прямой,
# проходящей через эти точки.
# a = 3
# print(f"    2 + 3\u000Ay = \u2015\u2015\u2015\u2015\u2015\u000A    3 x 4")

#запросим координаты точки 1
m1 = input('Введите координаты точки M1 в формате (x;y): ')
x1, y1 = map(int, m1.split(';'))

#запросим координаты точки 2
m2 = input('Введите координаты точки M2 в формате (x;y): ')
x2, y2 = map(int, m2.split(';'))

#urav = (y - y1) / (y2 - y1) = (x - x1) / (x2 - x1)
#вычисляем знаменатели
znam1 = y2 - y1
znam2 = x2 - x1

# znam1 *= -1
# znam2 *= -1

#znam2*(y - y1) = znam1 * (x - x1)

# print(f'{znam2}*(y - {y1}) = {znam1} * (x - {x1})')

#вычисляем значения с буквами
y = str(znam2) + 'y'
x = str(znam1 * -1) + 'x'

print('Решение:')
print('Уравнение пучка прямых, проходящих через точку М\u2081(x\u2081;y\u2081) имеет вид:')
print('y - y\u2081 = k(x - x\u2081)')
print('''где неизвестный коэффициент k определим из условия прохождения прямой 
М\u2081М\u2082 через точку М\u2082(x\u2082;y\u2082), т.е. координаты точки 
М\u2082 должны удавлетворять уравнению:''')
print('y\u2082 - y\u2081 = k(x\u2082 - x\u2081)')
print('отсюда')
#print(f"    y\u2082 - y\u2081\u000Ak = \u2015\u2015\u2015\u2015\u2015\u000A    x\u2082 - x\u2081")
print('k = y\u2082 - y\u2081 / x\u2082 - x\u2081')
print('Подставляя эту формулу в предыдущую, получим:')
#print('y - y\u2081\u000A\u2015\u2015\u2015\u2015\u2015\ = u000Ay\u2082 - y\u2081')
print('y - y\u2081 / y\u2082 - y\u2081 = x - x\u2081 / x\u2082 - x\u2081')
print('Это и есть искомое уравнение прямой, проходящей через дведанные точки.')
print('Подставим полученные координаты в уравнение:')
print(f'(y - {y2}) / ({y2} - {y1}) = (x - {x1}) / ({x2} - {x1})')
print('Решим уравнение')
print(f'(y - {y2}) / {y2 - y1} = (x - {x1}) / {x2 - x1}')
print(f'{znam2}*(y - {y1}) = {znam1} * (x - {x1})')
print(f'{y}-{znam2 * y1} = {x}+{znam1*x1}')

#выводим результат
print('Ответ:')

print(f'{x}+{y}+{x1 + y1}=0');
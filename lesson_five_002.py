# Написать программу сложения и умножения двух шестнадцатеричных чисел. При 
# этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. 
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. 
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

chisla_16 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15}

# polsovatel_1 = 'A2'
# polsovatel_2 = 'C4F'
polsovatel_1 = input('Введите первое число формата(A2): ')
polsovatel_2 = input('Введите второе число формата(A2): ')
total_chislo_rev = []

pol_list_1 = list(polsovatel_1)
pol_list_2 = list(polsovatel_2)

# метод проверки одинаковости длинны шестнадцатеричных чисел
def addition_chisla():
    pol_list_1.reverse()
    pol_list_2.reverse()
    if len(pol_list_1) < len(pol_list_2):
        dl = len(pol_list_2) - len(pol_list_1)
        for _ in range(dl):
            pol_list_1.append('0')
    elif len(pol_list_1) > len(pol_list_2):
        dl = len(pol_list_1) - len(pol_list_2)
        for _ in range(dl):
            pol_list_2.append('0')
    elif len(pol_list_1) == len(pol_list_2):
        print('числа равны')
    
    summ_chisel()

# поиск чисел
def find_key(f_vall):
    for key, vall in chisla_16.items():
        if f_vall > 9 and f_vall == vall:
            return key
        elif f_vall <= 9:
            return f_vall

# приводим к числовому значению
def summ_chisel():
    down_num = 0
    for i in range(len(pol_list_1)):
        if pol_list_1[i] in chisla_16:
            a = chisla_16[pol_list_1[i]]
            b = 0
            if pol_list_2[i] in chisla_16:
                b = chisla_16[pol_list_2[i]]
            else:
                b = int(pol_list_2[i])
        else:
            a = int(pol_list_1[i])
            b = 0
            if pol_list_2[i] in chisla_16:
                b = chisla_16[pol_list_2[i]]
            else:
                b = int(pol_list_2[i])
        print(f'{a} - {b}')

        vr_summ = a + b + down_num
        print(f'сумма {vr_summ}')
        if vr_summ > 16:
            top_num = vr_summ - 16
            down_num = 1
            total_chislo_rev.append(find_key(top_num))
            #total_chislo_rev.append(top_num)
        else:
            down_num = 0
            total_chislo_rev.append(find_key(vr_summ))
            #total_chislo_rev.append(vr_summ)
            top_num = 0

addition_chisla()
total_chislo_rev.reverse()
print(f'Сумма щестнадцатеричных чисел = {total_chislo_rev}')

# Попытка работы через десятичные числа. Неудачная.

# метод перевода шестнадцатиричного числа в десятичное
# def convert_to_ten(chislo):
#     summ = 0
#     chislo.reverse()
#     for i, vall in enumerate(chislo):
#         if vall in chisla_16:
#             a = chisla_16[vall] * (16**i)
#             summ += a
#             # print(a)
#         else:
#             a = int(vall) * (16**i)
#             summ += a
#             # print(a)
#     return summ

# total_chislo_1 = convert_to_ten(pol_list_1)
# print(f'число {polsovatel_1} это {total_chislo_1}')

# переведём числа в десятичную систему счисления
# ch_1 = convert_to_ten(pol_list_1)
# ch_2 = convert_to_ten(pol_list_2)

# print(ch_1)
# print(ch_2)

# найдём сумму чисел
# summ_ch = ch_1 + ch_2
# print(f'Сумма чисел {summ_ch}')
# print(summ_ch / 16)

# найдём произведение чисел
# mult_ch = ch_1 * ch_2
# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;'

my_str = 'beep boop beer!'

my_dict = {'2':{'r':0, '!':1}}

for i in alph:
    numm = my_str.count(i)
    if numm > 0:
        print(f'{i}: {numm}')
        my_dict.update({i:numm})
print(my_dict)
print(len(my_dict))
print(my_dict.get(1))

# for i, val in my_dict:
#     print(f'{i}: {i.isdigit()}')
print('Сдаю домашку так, как есть. Не получается придумать алгоритм обхода всех значений.')
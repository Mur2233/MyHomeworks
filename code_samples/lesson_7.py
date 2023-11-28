data_lst = ['1', '2', '3', '4d', 5, 'ffg', '5gf', 222, 67, 41, '34', 'gg']
# data_lst = input('Введите число: ')
new_list = []
result_list = []

for item in data_lst:
    try:
        item = int(item)
        result_list += str(item).split()
        # print(result_list)
    except ValueError:
        new_list += str(item).split()
        # print(f'Переменная(ые) {new_list} невалидна(ы)')
if result_list:
    print(f'Числа {result_list} прошли проверку')
raise ValueError(f'Переменная(ые) {new_list} невалидна(ы)')

# =========================================================
# numbers = ['+77053183958';'+77773183958';'87773183958';'+(777)73183958';'+7(777)-731-83-58';'+7(777) 731 83 58']

# +77053183958;+77773183958;87773183958;+(777)73183958;+7(777)-731-83-58;+7(777) 731 83 58

numbers = input('Введите номера через точку с запятой(;): ')
# print(numbers)
item = numbers.strip()
if item.strip():
    number_lst = (item.strip().
                  replace('+', '').
                  replace('(', '').
                  replace(')', '').
                  replace('-', '').
                  replace(' ', ''))
    verified_number = number_lst.split(';')
    # print(verified_number)

for symbol in verified_number:
    if symbol.isdigit():
        print(f'Номер {symbol} состоит только из чисел')
    else:
        raise ValueError(f'Номер {symbol} должен состоять только из чисел!')
    if len(symbol) == 11:
        print(f'Номер {symbol} проходит проверку на длину строки')
    else:
        raise ValueError(f'Номер {symbol} должен иметь больше 11 знаков')
    if symbol.startswith('7') or symbol.startswith('8'):
        print(f'Номер {symbol} проходит проверку на наличие верного символа')
    else:
        raise ValueError(f'Номер {symbol} должен начинаться с (+)7 или 8')

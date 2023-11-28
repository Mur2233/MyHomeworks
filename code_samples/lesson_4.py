# Задание 1

is_len_num = False
is_start = False
is_dig = False
res_num = ''

number = input('Введите номер телефона: ')

if len(number) >= 11:
    is_len_num = True
else:
    res_num += 'Номер должен иметь 11 символов\n'

if number.startswith('+7') or number.startswith('8') or number.startswith('+('):
    is_start = True
else:
    res_num += 'Номер должен иметь значение 8 или +\n'

if number.isdigit() or not number.isdigit():
    is_dig = True
else:
    res_num += 'Номер должен состоять из цифр\n'

if is_len_num and is_start and is_dig:
    res_num += 'Номер удовлетворяет значение\n'
else:
    res_num += 'Неправильно набран номер\n'

print(res_num)

# +77773183958
# 87773183958
# +(777)73183958
# +7(777)-731-83-58
# +7(777) 731 83 58

# =====================================================

# Задание 2

is_len = False
is_wer = False
is_strip = False
res_str = ''

password = input('Введите пароль: ')

if len(password) >= 7:
    is_len = True
else:
    res_str += 'Пароль должен иметь не менее 7 символов\n'

if not (password.islower() or password.isupper()):
    is_wer = True
else:
    res_str += 'В пароле должны быть символы разных регистров\n'

if password.strip():
    is_strip = True
else:
    res_str += 'Пробелы и другого рода символы не должны присутстовать\n'

if is_len and is_wer and is_strip:
    res_str += 'Пароль надёжен\n'
else:
    res_str += 'Придумайте пароль получше\n'

print(res_str)
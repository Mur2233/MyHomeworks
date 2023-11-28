word = input('Введите слово: ')
if word.upper() == word[::-1].upper():
    print('Это слово палиндром')
else:
    print(f'Слово "{word}" не является палиндромом, введите другое!')
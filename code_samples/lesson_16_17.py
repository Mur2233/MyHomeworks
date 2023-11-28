'''
10. Опционально: напишите аннотацию типов для переменных, в которых будет результат и пройдите проверку
mypy (оставьте сообщение в комментариях в коде об успешной проверке. Я всё читаю!)
11. Сделайте красивый принт результатов pprint с подписью, какое задание и где выполнено 💪 (помните, что
у него надо выключить сортировку, иначе он сортирует словарь еще раз)
'''
# =========================================================
from typing import (List, Dict, Set, Union, Optional, Any, Callable)
from  pprint import pprint

# 1. Сделайте импорт full_dict из документа Marvel.py
from marvel import full_dict


#  2. Напишите пользовательский ввод цифр через пробел, разбейте его на список, и примените к каждому
# элементу списка int используя map , но только в том случае, если этот элемент списка число, иначе
# замените его на None
print('Задание 2')
num_input: List[str] = input('Введите числа через пробел: ').split(' ')
num_input_map: List[int | None] = list(map(lambda num: int(num) if num.isdigit() else None, num_input))
pprint(num_input_map)

# 3. Используйте filter и получите аналогичный по структуре словарь, который будет содержать исходные id и
# остальные ключи, но только тех фильмов, id которых есть в полученном списке в п.2
print('Задание 3')
num_input_filter: dict = dict(filter(lambda num: num[0] in num_input_map, full_dict.items()))
pprint(num_input_filter)

# 4. Составьте set comprehension (генератор множества) собрав множество содержимого ключа director
# словаря дата-сета
print('Задание 4')
director_set_comprehension: set = {movie['director'] for movie in full_dict.values() if movie['director'] != 'TBA'}
pprint(director_set_comprehension)

# 5. Составьте dict comprehension (генератор словаря) сделав копию исходного словаря full_dict , при этом
# применим в к каждому 'year' значению, функцию str
print('Задание 5')
str_dict_comprehension: Dict[int, Dict[str, str]] = {key:
                                                      { 'title': value['title'],
                                                        'year': str(value['year']),
                                                        'director': value['director'],
                                                        'screenwriter': value['screenwriter'],
                                                        'producer': value['producer'],
                                                        'stage': value['stage'],}
                                                    for key, value in full_dict.items()}
pprint(str_dict_comprehension)

# 6. Используйте filter и получите аналогичный по структуре словарь, который будет содержать исходные id и
# остальные ключи, но только тех фильмов, которые начинаются на букву Ч
print('Задание 6')
id_filter: Dict[int, Dict[str, Any]] = dict(filter(lambda n: n[1]['title'].startswith('Ч'), full_dict.items()))
pprint(id_filter)

# 7. Сделайте сортировку словаря full_dict по одному (любому) параметру, с использованием lambda на выходе
# аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете сортировку!
print('Задание 7')
# Сортировку делаю по параметру screenwriter, возможно он не самый интересный, но куда деваться:)
screenwriter_lambda: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(),
                                                                    key=lambda n: n[1]['screenwriter']))
pprint(screenwriter_lambda, sort_dicts=False)

# 8. Опционально: сделайте сортировку словаря full_dict по двум (любом) параметрам, с использованием lambda
# на выходе аналогичный по структуре словарь. Обязательно подпишите, по какому параметру вы делаете
# сортировку!
print('Задание 8')
# Сортировку делаю по параметрам stage, title
year_title_lambda: Dict[int, Dict[str, str | int]] = dict(
    sorted(full_dict.items(), key=lambda n: (n[1]['stage'], n[1]['title']))) # !!! если записать за место stage -> year, то он будет ругаться, хотя значение str | int дано
pprint(year_title_lambda, sort_dicts=False)


# 9. Опционально: напишите однострочник, в котором мы получаем аналогичный по структуре full_dict но
# отфильтрованный через filter и с использованием в этой же строке sorted
print('Задание 9')
filter_sorted: Dict[int, Dict[str, str]] = dict(
    sorted(filter(lambda n: n[1]['title'].startswith('Ч'), full_dict.items()),
           key=lambda n: 3000 if n[1]['year'] == 'TBA' else n[1]['year']))
pprint(filter_sorted, sort_dicts=False)





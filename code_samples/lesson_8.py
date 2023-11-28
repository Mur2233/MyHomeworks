from marvel import full_dict
from pprint import pprint

# ==============================================

# for item in full_dict:
    # phase_in_numbers = input('Введите цифрами фазу: ')
    # if phase_in_numbers.isdigit():
    #     phase_count = int(phase_in_numbers)
    #     if phase_count > item:
    #         raise ValueError('Такой фазы не существует\n'
    #                          f'Будет выведено {item} фаз')
    #         phase_count = item
    #     else:
    #         raise TypeError('Ожидаем получение числа')
    #         pprint(item)


# ====================================================

stage = {
    1: 'Первая фаза',
    2: 'Вторая фаза',
    3: 'Третья фаза',
    4: 'Четвёртая фаза',
    5: 'Пятая фаза',
    6: 'Шестая фаза',
}

input_phase_stage = input('Введите номер фазы: ')
if not input_phase_stage.isdigit():
    raise TypeError('Вы ввели не число')

user_stage = int(input_phase_stage)

if user_stage not in stage.keys():
    raise ValueError('Такой фазы не существует\n'
                    f'Будет выведено {full_dict.items()}')

stage_string = stage[user_stage]

# result = {film_dict['title']
#           for film, film_dict in full_dict.items()
#           if film_dict['stage'] == stage_string}
# pprint(result) # Пример учителя

for film, film_dict in full_dict.items(): # не пойму, для чего нужна переменная film,
    if film_dict['stage'] == stage_string: # но без неё код отказывается работать
        pprint(film_dict)





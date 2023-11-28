'''
1. Вам нужен, хотя бы частично, код из прошлого задания.
2. Получите сет городов (это п.6 прошлого задания)

3. Напишите код, который запишет этот сет в JSON
4. Закомментируйте код из пунктов выше. Я должен видеть, что вы умеете писать в JSON
5. Сделайте код, который будет читать данные из JSON и загружать нам сразу готовый датасет
'''
# from cities import cities_list
# from pprint import pprint
#
# cities_set = set()
#
# for city in cities_list:
#     if city['name'][-1].lower() not in 'ъьы':
#         cities_set.add(city['name'])
# # pprint(cities_set)
#
import json
#
# with open('cities.json', 'w', encoding='utf=8') as file:
#     json.dump(list(cities_set), file, ensure_ascii=False, indent=4)

with open('cities.json', 'r', encoding='utf-8') as file:
    cities_set = set(json.load(file))

# print(len(cities_set))

# Ход компьютера
computer_city = None

while cities_set:
    # Пользовательский ввод
    input_city = input('Введите город: ').strip()
    # Проверка на стоп
    if input_city == 'стоп':
        print('Вы проиграли')
        break

    # Проверяем, что этот город есть в списке
    if input_city not in cities_set:
        print('Такого города нет в списке городов.\n'
              'Вы проиграли!')
        break

    # Если компьютер уже ходил. Делаем проверку на последнюю букву
    if computer_city:
        if computer_city[-1].lower() != input_city[0].lower():
            print('Город начинался с другой буквы. Вы проиграли')
            break
    # Удаление из сета(ход человека)
    cities_set.remove(input_city)

    # Ход компьютера
    for city in cities_set:
        if city[0].lower() == input_city[-1].lower():
            computer_city = city
    # Удаление из сета(ход компьютера)
    cities_set.remove(computer_city)
    # Ход компьютера
    print(f'Второй игрок(бот): {computer_city}')
else:
    print('Игра окончена. Вы выиграли!')








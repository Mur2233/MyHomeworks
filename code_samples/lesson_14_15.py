import json
from typing import (List, Dict, Tuple, Set, Union, Optional, Any, Callable)

def get_city(file_name: str = 'cities.json') -> set:
    """
    Читаем файл json
    :param file_name: 'cities.json'
    :return: Сет городов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        cities_set = set(json.load(file))
    return cities_set

def check_game(last_round_city: str, current_round_city: str) -> bool:
    """
    Функция принимает два города и проверяет, что первая буква города current_round_city
    равна последней букве города last_round_city
    :param last_round_city: Город из прошлого раунда
    :param current_round_city: Город из текущего раунда
    :return: bool
    """
    if last_round_city[-1].lower() == current_round_city[0].lower():
        return True
    else:
        return False

def computer_move(cities_set: set, last_round_city: str) -> str | None:
    """
    Функция принимает список городов и город из прошлого раунда.
    Проходится списком по сету городов и производит проверку.
    :param cities_set: Список городов
    :param last_round_city: Город из прошлого раунда
    :return: Проверка
    """
    for city in cities_set:
        if check_game(last_round_city, city):
            return city
    else:
        return None


def main():
    """
    Функция проходится по циклу, воспроизводя игру
    :param: input_city: Ход человека
    :param: computer_city: Ход компьютера
    :return: Итог игры
    """
    # cities_set = get_city()
    cities_set: Set[str] = get_city()
    # computer_city = None
    computer_city: Optional[str] = None


    while cities_set:
        # Пользовательский ввод
        input_city = input('Первый игрок, введите город: ').strip()

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
            if not check_game(computer_city, input_city):
                print('Город начинался с другой буквы. Вы проиграли.')
                break

        # Удаление из сета(ход человека)
        cities_set.remove(input_city)
        print(f'Вы ввели: {input_city}')

        # Ход компьютера
        # computer_city = computer_move(cities_set, input_city)
        computer_city: List[str] = computer_move(cities_set, input_city)

        if not computer_city:
            print('Игра окончена. Вы выиграли!')
            break
        # Удаление из сета(ход компьютера)
        cities_set.remove(computer_city)
        print(f'Компьютер ввёл: {computer_city}')
    else:
        print('Игра окончена. Вы выиграли!')

main()

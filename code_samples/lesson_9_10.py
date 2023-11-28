from cities import cities_list

shadatha = """
6. Наполните его названиями городов перебор списка словарей импортированного в п.4 cities любым из пройденных
способов
1. Объявите цикл while
2. Объявите пользовательский ввод
3. Сделайте проверку на стоп. Если пользователь ввёл стоп - он проиграл машине.

4. Сделайте проверку, что это название есть в сете городов (Если нет - вероятно вы проиграли машине)
5. Если есть. Удалите его из сета
6. Придумайте, как можно реализовать проверку условий выполнения игры (подходит ли ответ пользователя, согласно тому
городу, который озвучил компьютер?)
7. Пусть компьютер теперь сделает свой ход. Поищет город, который кончается на последнюю букву того города, который
назвали вы.
8. Если такой город есть - повторите цикл.
9. В конце игры, объявите победителя.

"""
cities_set = set()  # Пустой сет

empty_list = []
symbols_bad = {"ь", "ъ", "ы"}

for cities in cities_list:
    cities_set.add(cities['name'])

print("Игра в города. Что бы закончить игру, введите слово стоп")
game_over = False

# Первый ход сделает компьютер, чтобы от него можно было отталкиваться дальше
city = 'Москва'
print(city)
# Помечаем, что следующий ход делает человек
step = 'human'
empty_list.append(city)
character_end = city[-1]

while game_over == False:
    if step == 'human':
        correct = False
        while correct == False:
            city = input("Следующий город начинается на букву: " + character_end + ". Введите название города: ")
            # Проверка на слово "стоп"
            if city == "стоп":
                game_over = True
                correct = True
                break
            else:
                correct = True
                # Проверяем, что город на нужную букву
                if city[0].lower() != character_end:
                    correct = False
                    print(f"Не верно. Назовите город на букву {character_end}")

                # Проверяем, что этот город есть в списке
                if city in cities_set:
                    pass
                else:
                    correct = False
                    print('Такого города нет в списке городов.\n'
                          'Вы проиграли!')
                    break
                # Проверяем, что этот город ещё не упоминался
                if city in set(empty_list):
                    correct = False
                    print('Такой город уже называли.\n'
                          'Вы проиграли!')
                    break
        # else:
        #     break

        step = 'comp'
    else:
        city = ''
        for city_next in cities_set:
            if city_next[0].lower() == character_end:
                city = city_next

        if city == '':
            print('Вы победили')
            print(f'Город на букву {character_end} не был найден')
            game_over = True
        else:
            print(city)

        step = 'human'

    if game_over == False:
        cities_set.remove(city)
        empty_list.append(city)

        character_end = city[-1]

        if character_end in symbols_bad:
            character_end = сity[-2]

        if character_end in symbols_bad:
            character_end = city[-3]
    else:
        pass
print('Игра окончена')







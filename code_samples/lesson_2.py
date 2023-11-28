# Задание 1

quantity_seconds = int(input('Введите количество секунд: '))
hour = quantity_seconds // 3600
minute = (quantity_seconds - hour * 3600) // 60
second = (quantity_seconds - hour * 3600)
result = f'Количество часов: {hour} \nКоличество минут: {minute} \nКоличество секунд: {second}'
print(result)

# Задание 2

sum_degrees = int(input('Введите количество градусов: '))
degrees_kelvin = sum_degrees + 273.15
degrees_fahrenheit = 1.8 * sum_degrees + 32
degrees_reomure = sum_degrees * 0.8
result_degrees = f'Градусов Кельвина: {degrees_kelvin} \nГрадусов Фаренгейта: {degrees_fahrenheit} \nГрадусов Реомюра: {degrees_reomure}'
print(result_degrees)
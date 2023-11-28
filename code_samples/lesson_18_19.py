from typing import (List, Dict, Tuple, Set, Union, Optional, Any, Callable)
import csv

''' Задача 1 '''

def password_cheked(func: Callable) -> Callable:
    def wrapper(password: str) -> str:
        if len(password) < 8:
            raise ValueError('Длина пароля должна быть не менее 8 символов.')
        if not any(map(str.isdigit, password)):
            raise ValueError('Пароль должен содержать хотя бы одну цифру.')
        if not any(map(str.isupper, password)):
            raise ValueError('Пароль должен содержать хотя бы одну заглавную букву.')
        if not any(map(str.islower, password)):
            raise ValueError('Пароль должен содержать хотя бы одну строчную букву.')
        if not any(map(lambda x: x in '!@#$%^&*()_-+=', password)):
            raise ValueError('Пароль должен содержать хотя бы один спецсимвол.')
        return func(password)

    return wrapper


@password_cheked
def register_user_num(password: str) -> str:
    return f'Пользователь зарегистрирован с паролем {password}'


print(register_user_num('sfdg3254GEf3$%'))

# print(register_user_num('SDGhnf54'))
# print(register_user_num('SDGhnf@'))


''' Задача 2 '''


def username_validator(func: Callable) -> Callable:
    '''
    Декоратор для валидации имени пользователя.
    :param func: функция обёртка.
    :return: обёрнутая функция.
    '''
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError('В имени пользователя не должно быть пробелов.')
        return func(username, password)

    return wrapper


def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1,
                       min_special_chars: int = 1) -> Callable:
    '''
    Декоратор для валидации паролей.
    :param min_length: Минимальная длина пароля (по умолчанию 8).
    :param min_uppercase: Минимальное количество букв верхнего регистра (по умолчанию 1).
    :param min_lowercase:  Минимальное количество букв нижнего регистра (по умолчанию 1).
    :param min_special_chars:  Минимальное количество спец-знаков (по умолчанию 1).
    :return: обёрнтая функция.
    '''
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError(f'Длина пароля должна быть не менее {min_length} символов.')
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                raise ValueError(f'Пароль должен содержать не менее {min_uppercase} символов в верхнем регистре')
            if sum(1 for char in password if char.islower()) < min_lowercase:
                raise ValueError(f'Пароль должен содержать не менее {min_uppercase} символов в нижнем регистре')
            if sum(1 for char in password if char.isalnum()) < min_special_chars:
                raise ValueError(f'Пароль должен содержать не менее {min_uppercase} спец-символов')
            return func(username, password)
        return wrapper
    return decorator


@username_validator
@password_validator()
def register_user(username: str, password: str) -> None: # категорически отказывался сотрудничать и принимать значения
    '''
    Функция для регистрации пользователей.
    :param username: имя пользователя.
    :param password: пароль пользователя.
    :return: None
    '''
    def wrapper(username: str, password: str) -> None:
        with open('user.csv', 'a', encoding='windows-1251') as f:
            f.write(f'{username}, {password}\n')
    return wrapper

try:
    register_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Мы справились... @-@"



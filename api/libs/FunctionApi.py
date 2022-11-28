from .Api import Api
import random
import string
import requests
from datetime import datetime

global lecturer, prev_lecturer
global conference


def prepare_arrays_assistant(in_conf):
    for pos in range(len(in_conf)):
        if in_conf[pos] == 'lecturer':
            in_conf[pos] = lecturer
        if in_conf[pos] == 'lastlecturer':
            in_conf[pos] = prev_lecturer
        if in_conf[pos] == 'auto':
            in_conf[pos] = ""
    return in_conf


def prepare_arrays(conf, personal=False, user=None):
    if not personal:
        position = Api().get_layout_position(conf)['position']
        return prepare_arrays_assistant(position['position']), position['nowSreen']
    elif personal:
        position = Api().get_personal_layout_position(conf, user)
        return prepare_arrays_assistant(position['position']), position['nowScreen']


def compare_position_assistant(in_conf, on_screen):
    for item in range(min(len(in_conf), len(on_screen))):
        if in_conf[item] != '' and on_screen[item] != '':
            if not (in_conf[item] in on_screen[item]):
                return False
    return True


# Сравнивает позиции плееров на экране с общей раскладкой
def compare_position_in_layout(conf, personal=False, user=None):
    if not personal:
        pos_in_conf, pos_on_screen = prepare_arrays(conf, personal)
        return compare_position_assistant(pos_in_conf, pos_on_screen)
    elif personal:
        pos_in_conf_personal, pos_on_screen_personal = prepare_arrays(personal, user)
        return compare_position_assistant(pos_in_conf_personal, pos_on_screen_personal)


def generate_random_string(length):
    """генерим случайную строку, на вход длина строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def data_time_stamp(sec=3600.0):
    """Генерируем """
    data = datetime.now()
    data = datetime.timestamp(data)
    data = data + float(sec)
    return datetime.fromtimestamp(data)


def data_in_time_stamp(sec=3600.0):
    data = datetime.now()
    data = datetime.timestamp(data)
    data = data + float(sec)
    return data


def add_array_mosaic():
    a = []
    for i in range(100):
        a.append('')
    return a


def assert_expected_result(response, field, expected_value_field, expected_code=201):
    """Проверка статус кода, проверка изменения поля в ответе сервера, проверка невалидных данных,
    на вход: ответ сервера, поле - значение которого нужно получить, ожидаемый результат значения поля в ответе,
    ожидаемый статус код"""
    data = response.json()
    response_value = give_value_response(data, field)
    if expected_code // 100 == 2:

        assert response.status_code == expected_code, \
            f"Статус код {response.status_code} отличается от ожидаемого {expected_code}, response = {response.json()}"

        assert response_value[0] == expected_value_field or str(response_value[0]) == expected_value_field,\
            f"Поле {field} не изменилось на ожидаемое {expected_value_field}, response = {response.json()}"
    elif expected_code == 422:
        assert response.status_code == 422, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    elif expected_code == 500:
        assert response.status_code == 500, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


def give_value_response(data, field):
    """На вход словарь и поле, значение которого хотим получить"""
    fields_found = []

    for key, value in data.items():
        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = give_value_response(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = give_value_response(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)
    return fields_found


def acc_num_generation() -> int:
    """Генерирует номер для аккаунта"""
    return random.randint(100000, 999999)


def conf_num_generation() -> int:
    """Генерирует номер для конференции"""
    return random.randint(10000, 99999)


def get_value(response, key, index=0):
    """Возвращаем только первое найденное значение или по индексу"""
    try:
        _json = response.json()
        _status_code = response.status_code
        values = give_value_response(_json, key)
        if len(values) == 0:
            raise NameError(f'Не удалось получить значение по ключу --- {values}')
        else:
            return values[index]
    except requests.JSONDecodeError:
        _status_code = response.status_code


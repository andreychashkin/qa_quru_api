import time

import allure
import pytest
from api import *


@pytest.fixture()
def created_accounts():
    api = Api()
    """Фикстура создает 5 аккаунтов с паролем 123456 и возвращает их номера в массиве"""
    arr = []
    with allure.step('Создаем аккаунты на сервере с паролями 123456'):
        for i in range(2):
            number = api.create_account(description=generate_random_string(5),
                                        password=TestData.password,
                                        number=acc_num_generation())
            arr.append(get_value(number, 'number'))
    yield arr
    with allure.step('Очищаем сервер'):
        for i in arr:
            api.delete_account(i)


@pytest.fixture()
def created_conferences():
    api = Api()
    """Фикстура создает 2 конференции с плеерами и одним участником,
    возвращает конференцию и номер участника, модератора"""
    with allure.step('Создаем модератора для первой конференции'):
        moderator = api.create_account(description='moderator',
                                       password=TestData.password,
                                       number=acc_num_generation())
        moderator = get_value(moderator, 'number')
    with allure.step('Создаем две конференцию'):
        conf_arr = []
        for i in range(2):
            conf = api.create_conference(description=generate_random_string(5), moderators=[moderator],
                                         number=conf_num_generation(), active=True)
            conf_arr.append(get_value(conf, 'number'))
    with allure.step('Создаем аккаунт и добавляем его в конфу'):
        account = api.create_account(password=TestData.password, ip=api.second_ip_server,
                                     number=acc_num_generation(), conferences=[conf_arr[0]])
        account = get_value(account, 'number')
    with allure.step('Добавляем плееров в конференцию'):
        api.add_players(conf_arr[0], ['video1', 'video2', 'video3'])
        api.add_players(conf_arr[1], ['video1'])
        time.sleep(1)
    yield {'conferences': conf_arr, 'participant': account, 'moderator': moderator}
    with allure.step('Очищаем сервер от созданных данных'):
        api.delete_conference(conf_arr[0])
        api.delete_conference(conf_arr[1])
        api.delete_account(moderator)
        api.delete_account(account)

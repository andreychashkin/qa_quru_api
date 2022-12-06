import allure
import pytest
from api import *


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Изменение настроек аккаунта')
@pytest.mark.parametrize('test_data', [
    ['description', generate_random_string(130), 200],
    ['description', True, 422],
    ['description', generate_random_string(131), 422],
    ['description', '', 422],

    ['password', '123456', 200],
    ['password', generate_random_string(10), 200],
    ['password', generate_random_string(1), 422],
    ['password', True, 422],

    ['email', 'test@email.com', 200],
    ['email', True, 422],
    ['email', 123, 422],

    ['bandwidth', 256, 200],
    ['bandwidth', True, 422],
    ['bandwidth', 10000, 422],

    ['ip', '10.1.0.11', 200],
    ['ip', True, 422],
    ['ip', 123213, 422],

    ['codecs', ['g7221', 'ulaw', 'h265', 'h264'], 200],
    ['codecs', False, 422],
    ['codecs', "['g7221','ulaw','h265','h264']", 422]
])
def test_accounts_change_settings(created_accounts, test_data):
    account = created_accounts[0]
    param, value, rez = test_data
    with allure.step('Выполняем запрос на изменение настроек аккаунта'):
        response = BaseApi().call_method('patch', f'api/v1/account/{account}', data={param: value, 'type': 'SIP'})
    assert_expected_result(response, param, value, rez)


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Изменение настроек аккаунта без авторизации на сервере response = 401')
def test_accounts_change_settings_401(created_accounts):
    account = created_accounts[0]
    with allure.step('Выполняем запрос на изменение настроек аккаунта без авторизации'):
        response = BaseApi(logins='test_test').call_method('patch', f'api/v1/account/{account}',
                                                           data={'description': 'test'})
    assert response.status_code == 401, \
        f'Ответ от сервера отличается от ожидаемого при изменении ' \
        f'настрое абонента --- {account}, response --- {response.json()}'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Изменение настроек несуществующего аккаунта response = 404')
def test_accounts_change_settings_404(created_accounts):
    with allure.step('Выполняем запрос на изменение настроек несуществующего аккаунта --- 8793249832'):
        response = BaseApi().call_method('patch', f'api/v1/account/8793249832', data={'description': 'test'})
    assert response.status_code == 404, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Изменение настроек аккаунта - ошибка доступа response = 403')
def test_accounts_change_settings_403(created_accounts):
    account = created_accounts[0]
    with allure.step('Выполнение запроса на изменение настроек аккаунта под аккаунтом'):
        response = BaseApi(logins=created_accounts[1]).call_method(
            'patch', f'api/v1/account/{account}', data={'description': 'test'})
    assert response.status_code == 403, \
        f'Ответ от сервера отличается от ожидаемого при изменении настроек аккаунта {account} ' \
        f'--- response = {response.json()}'

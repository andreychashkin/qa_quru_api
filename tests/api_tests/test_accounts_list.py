import allure
from api import *


@allure.id("12598")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Запрос списка аккаунтов доступных для добавления в указанную конференцию response = 200')
def test_allowed_accounts_in_conf_200(created_accounts, created_conferences):
    conf = created_conferences['conferences'][0]
    with allure.step('Выполняем запрос списка аккаунтов для добавления в конференцию'):
        response = AccountsApi().api_test('get', f'api/v1/allowed_accounts/{conf}')
    assert response.status_code == 200, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12599")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Получение списка аккаунтов response = 200')
def test_accounts_list_200(created_accounts):
    with allure.step('Выполняем запрос на получение списка аккаунтов'):
        response = AccountsApi().api_test('get', 'api/v1/accounts')
    assert response.status_code == 200, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12600")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Получение списка аккаунтов без авторизации response = 401')
def test_accounts_list_401(created_accounts):
    with allure.step('Выполняем запрос на получение списка аккаунтов'):
        response = AccountsApi(logins='test_test').api_test('get', 'api/v1/accounts')
    assert response.status_code == 401, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12601")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Получение списка аккаунтов ошибка доступа response = 403')
def test_accounts_list_403(created_accounts):
    with allure.step(f'Выполняем запрос на получение списка абонентов авторизовавшись под аккаунтов'):
        response = AccountsApi(logins=created_accounts[0]).api_test('get', 'api/v1/accounts')
    assert response.status_code == 403, f"Ответ сервера отличается от ожидаемого response = {response.json()}"

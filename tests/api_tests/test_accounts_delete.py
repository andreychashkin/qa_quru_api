import allure
from api import *


@allure.id("12591")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление аккаунта response = 200')
def test_delete_account_200(created_accounts):

    with allure.step(f'Выполняем запрос на удаление аккаунта'):
        response = BaseApi().api_test('delete', f'api/v1/account/{created_accounts[0]}')
    assert response.status_code == 200, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12592")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление несуществующего аккаунта response = 404')
def test_delete_account_404(created_accounts):
    with allure.step('Выполняем запрос на удаление несуществующего аккаунта'):
        response = BaseApi().api_test('delete', f'api/v1/account/{generate_random_string(10)}')
    assert response.status_code == 404, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12593")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление аккаунта без авторизации response = 401')
def test_delete_account_401(created_accounts):
    with allure.step('Выполняем запрос на удаление аккаунта без авторизации'):
        response = BaseApi(logins='test_test').api_test('delete', f'api/v1/account/{created_accounts[0]}')
    assert response.status_code == 401, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12594")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление аккаунта с ошибкой доступа response = 403')
def test_delete_account_403(created_accounts):
    with allure.step(f'Выполняем запрос на удаление аккаунта авторизовавшись под accounts'):
        response = BaseApi(logins=created_accounts[1]).api_test('delete', f'api/v1/account/{created_accounts[0]}')
    assert response.status_code == 403, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12595")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление выбранных аккаунтов response = 200')
def test_delete_accounts_200(created_accounts):
    with allure.step(f'Выполняем запрос на удаление выбранных аккаунтов -- []'):
        response = BaseApi().api_test('post', 'api/v1/delete_accounts', numbers=created_accounts)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12596")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление аккаунтов без авторизации response = 401')
def test_delete_accounts_401(created_accounts):
    with allure.step('Выполняем запрос на удаление нескольких аккаунтов [] без авторизации'):
        response = BaseApi(logins='test_test').api_test('post', 'api/v1/delete_accounts', numbers=created_accounts)
    assert response.status_code == 401, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12597")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Удаление аккаунтов Ошибка доступа response = 403')
def test_delete_accounts_403(created_accounts):
    with allure.step(f'Выполняем запрос на удаление нескольких аккаунтов []  под пользователем'):
        response = BaseApi(logins=created_accounts[0]).api_test('post', 'api/v1/delete_accounts', numbers=created_accounts)
    assert response.status_code == 403, f"Ответ сервера отличается от ожидаемого response = {response.json()}"

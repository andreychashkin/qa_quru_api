import allure
from api import *


@allure.id("12626")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Получение настроек аккаунта response = 200')
def test_get_settings_account_200(created_accounts):
    with allure.step('Выполняем запрос на получение настроек аккаунта'):
        response = AccountsApi().get_data_account(created_accounts[0])
    assert response.status_code == 200, f'Ответ сервера отличается от ожидаемого -- f{response.json()}'


@allure.id("12627")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Получение настроек аккаунта пустой запрос, response  = 404')
def test_get_settings_account_404(created_accounts):
    with allure.step('Выполняю пустой get запрос на получение настроек аккаунта'):
        response = AccountsApi().get_data_account(None)
    assert response.status_code == 404, f'Ответ сервера отличается от ожидаемого при' \
                                        f' отправке пустого запроса -- f{response.json()}'


@allure.id("12628")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Получение настроек аккаунта без авторизации response = 401')
def test_get_settings_account_401(created_accounts):
    with allure.step('Выполняем запрос получения настроек абонента без авторизации на сервере'):
        response = AccountsApi(logins='test_test').get_data_account(created_accounts[0])
    assert response.status_code == 401, f"Ответ сервера отличается от ожидаемого response = {response.json()}"

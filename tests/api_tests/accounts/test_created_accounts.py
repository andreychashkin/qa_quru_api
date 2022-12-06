import allure
import pytest

from api import *


@pytest.fixture()
def number():
    with allure.step('Генерируем рандомный номер для аккаунта'):
        number = random.randint(10000, 99999)
    yield number
    with allure.step('Очистка сервера'):
        AccountsApi().delete_account(number)


@allure.id("12606")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с валидным номером response = 201')
@pytest.mark.parametrize('number', ['dsfggfdsgvc', "410300"])
def test_created_accounts_number_201(number):
    with allure.step('Выполняем запрос на создание аккаунта с валидным номером'):
        response = BaseApi().api_test('post', 'api/v1/accounts', number=number)
    with allure.step('Удаление аккаунта'):
        AccountsApi().delete_account(number)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого при создании аккаунта --- {number}," \
                                        f" response --- {response.json()}"
    assert number in response.json()['data']['account']['number'], 'Номер созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта разных типов 201')
@pytest.mark.parametrize('types', ['SIP', 'H323', 'WS', 'Loop'])
def test_created_accounts_type_201(number, types):
    with allure.step('Выполняем запрос на создание аккаунта с указанием протокола'):
        response = BaseApi().api_test('post', 'api/v1/accounts', type=types, number=number)
    with allure.step('Удаление аккаунта'):
        AccountsApi().delete_account(number)
    assert response.status_code == 201, \
        f"Ответ сервера отличается от ожидаемого при создании аккаунта --- {number} с протоколом {types}"
    assert response.json()['data']['account']['type'] == types, 'Тип созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с разным описанием response = 201')
@pytest.mark.parametrize('description', ["TestName", "test_", "test_123", "10300", "name.name",
                                         "тест.тест", "тест123", "тест тест", "тест_", "Тест"])
def test_created_accounts_description_201(number, description):
    with allure.step('Выполняем запрос на создание аккаунта с валидным описанием'):
        response = BaseApi().api_test('post', 'api/v1/accounts', description=description, number=number)
    assert response.status_code == 201, \
        f"Ответ сервера отличается от ожидаемого при создании абонента {number}, с описанием {description}"
    assert description in response.json()['data']['account']['description'], \
        'Описание созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с различными паролями response = 201')
@pytest.mark.parametrize('password', list("`!A#$&'()*+,-./01z;[{<|=]}>^?_"))
def test_created_accounts_password_201(number, password):
    with allure.step("Выполняем запрос на создание аккаунта с указанием валидного пароля"):
        response = BaseApi().api_test('post', 'api/v1/accounts', password=f'abc{password}', number=number)
    assert response.status_code == 201, \
        f"Ответ сервера отличается от ожидаемого при создании аккаунта {number} с паролем {password}"
    assert password in response.json()['data']['account']['password'], \
        'Описание созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с различными email response = 201')
@pytest.mark.parametrize('mail',
                         ['simple@example.com',
                          'very.common@example.com',
                          'disposable.style.email.with@example.com',
                          'fully-qualified-domain@example.com']
                         )
def test_created_accounts_email_201(number, mail):
    with allure.step('Выполняем запрос на создание аккаунта с указанием почты'):
        response = BaseApi().api_test('post', 'api/v1/accounts', email=mail, number=number)
    assert response.status_code == 201, f"Отвеет сервера отличается от ожидаемого при создании аккаунта с почтой {mail}"
    assert mail in response.json()['data']['account']['email'], \
        'Email созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с различной шириной канала response = 2-1')
@pytest.mark.parametrize('bandwidth', ['64', '128', '1536'])
def test_created_accounts_bandwidth_201(number, bandwidth):
    with allure.step('Выполняем запрос на Создание аккаунта с указанием ширины канала'):
        response = BaseApi().api_test('post', 'api/v1/accounts', bandwidth=bandwidth, number=number)
    assert response.status_code == 201, f"Не удалось создать аккаунт {number} на сервере с шириной канала {bandwidth}"
    assert int(bandwidth) == response.json()['data']['account']['settings']['bandwidth'], \
        'Ширина канала созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с различными разрешениями p2p response = 201')
@pytest.mark.parametrize('resolution', ['CIF', '720p'])
def test_created_accounts_resolution_201(number, resolution):
    with allure.step('Выполняем запрос на создание аккаунта с указанием p2p разрешения'):
        response = BaseApi().api_test('post', 'api/v1/accounts', resolution=resolution, number=number)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого, response = {response.json()}"
    assert resolution in response.json()['data']['account']['settings']['resolutionP2P'], \
        'Разрешение видео потока созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с различными разрешениями для конференций response = 201')
@pytest.mark.parametrize('defaultResolution', ['1024x576', 'CIF', '720p'])
def test_created_accounts_default_resolution_201(number, defaultResolution):
    with allure.step('Выполняем запрос на создание аккаунта с указанием defaultResolution'):
        response = BaseApi().api_test('post', 'api/v1/accounts', defaultResolution=defaultResolution, number=number)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    assert defaultResolution in response.json()['data']['account']['settings']['defaultResolution'], \
        'Разрешение видео потока созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с настройкой опции Nat для h323 and sip accounts response = 201')
@pytest.mark.parametrize('types', ['SIP', 'H323'])
@pytest.mark.parametrize('behindNat', ['no', 'yes', pytest.param('never', marks=pytest.mark.xfail())])
def test_created_accounts_behind_nat_201(number, behindNat, types):
    with allure.step('Выполняем запрос на создание аккаунта с указанием type и behindNat'):
        response = BaseApi().api_test('post', 'api/v1/accounts', behindNat=behindNat, number=number, type=types)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого --- response = {response.json()}"
    assert behindNat in response.json()['data']['account']['settings']['behindNat'], \
        'Настройка проключать видеокодеки видео потока созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с настройкой опции ip response = 201')
@pytest.mark.parametrize('types', ['SIP', 'H323'])
@pytest.mark.parametrize('ip', ['10.1.0.11', '0.0.0.0'])
def test_created_accounts_ip_201(number, ip, types):
    with allure.step('Выполняем запрос на создание аккаунта с указанием валидного ip'):
        response = BaseApi().api_test('post', 'api/v1/accounts', ip=ip, number=number, type=types)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    assert ip in response.json()['data']['account']['settings']['ip'], \
        'Настройка ip созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта с настройкой опции port response = 201')
@pytest.mark.parametrize('types', ['SIP', 'H323'])
@pytest.mark.parametrize('port', [5061, 1132, 123213])
def test_created_accounts_port_201(number, port, types):
    with allure.step('Выполняем запрос на создание аккаунта с указанием валидных type и port'):
        response = BaseApi().api_test('post', 'api/v1/accounts', port=port, number=number, type=types)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    assert port == response.json()['data']['account']['settings']['port'], \
        'Настройка port созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта SIP с настройкой опцией транспортного протокола response = 201')
@pytest.mark.parametrize('transport', ['UDP', 'TCP', 'TLS'])
def test_created_accounts_transport_201(number, transport):
    with allure.step('Выполняем запрос на создание аккаунта с указанием transport'):
        response = BaseApi().api_test('post', 'api/v1/accounts', transport=transport, number=number, type='SIP')
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    assert transport in response.json()['data']['account']['settings']['transport'], \
        'Настройка port созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта SIP с настройкой опцией транспортного протокола response = 201')
@pytest.mark.parametrize('insecure', ['port', 'invite', 'very'])
def test_created_accounts_insecure_201(number, insecure):
    with allure.step('Выполняем запрос на создание аккаунта с указанием insecure'):
        response = BaseApi().api_test('post', 'api/v1/accounts', insecure=insecure, number=number, type='SIP')
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    assert insecure in response.json()['data']['account']['settings']['insecure'], \
        'Настройка insecure созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта SIP с настройкой bfcpType response = 201')
@pytest.mark.parametrize('bfcpType', ['UDP', 'TCP', 'NONE'])
def test_created_accounts_bfcp_type_201(number, bfcpType):
    with allure.step('Выполняю запрос на создание аккаунта SIP с указанием bfcpType'):
        response = BaseApi().api_test('post', 'api/v1/accounts', bfcpType=bfcpType, number=number, type='SIP')
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json}"
    assert bfcpType in response.json()['data']['account']['settings']['bfcpType'], \
        'Настройка insecure созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта SIP H323 с настройкой dtmf response = 201')
@pytest.mark.parametrize('types', ['SIP', 'H323'])
@pytest.mark.parametrize('dtmf', ['rfc2833', 'auto', 'inband', 'info'])
def test_created_accounts_dtmf_201(number, types, dtmf):
    with allure.step('Выполняем запрос на создание аккаунта с указанием types и dtmf'):
        response = BaseApi().api_test('post', 'api/v1/accounts', dtmf=dtmf, number=number, type=types)
    assert response.status_code == 201, f"Ответ сервера отличается от ожидаемого response = {response.json()}"
    assert dtmf in response.json()['data']['account']['settings']['dtmf'], \
        'Настройка insecure созданного аккаунта отличается от заданного'


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта авторизовавшись абонентом response = 403')
def test_created_accounts_403(number, created_accounts):
    with allure.step('Выполняем запрос авторизовавшись под аккаунтом'):
        response = BaseApi(logins=created_accounts[0]).api_test('post', 'api/v1/accounts')
    assert response.status_code == 403, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта без авторизации response = 401')
def test_created_accounts_401(number):
    with allure.step('Выполняем запрос на создание аккаунта без авторизации на сервере'):
        response = BaseApi(logins='test_test').api_test('post', 'api/v1/accounts')
    assert response.status_code == 401, f"Ответ сервера отличается от ожидаемого response = {response.json()}"

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


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта SIP и сравнение с дефолтными настройками response = 201')
def test_created_account_compare_with_default_sip_201(number):
    number = number
    with allure.step('Выполняем запрос на создание аккаунта и сравниваем с эталоном'):
        response = BaseApi().api_test('post', 'api/v1/accounts', number=number, type="SIP", password='123').json()
    default_acc = {'account': {'addressBookContact': None, 'description': str(number), 'number': str(number),
                               'type': "SIP", 'password': '123', 'email': '', 'source': 'local', 'tenant': None,
                               'group': None, 'groups': [], 'settings':
                                   {'bandwidth': 1536, 'resolutionP2P': '720p', 'behindNat': 'no', 'ip': 'dynamic',
                                    'port': 5060, 'transport': 'UDP', 'insecure': 'port', 'qualify': True,
                                    'codecs': ['g7221', 'ulaw', 'h265', 'h264'], 'h264HighProfile': False,
                                    'h239sendContentInMainStream': False, 'mediaStreams': False, 'dtmf': 'rfc2833',
                                    'bfcpType': 'UDP',
                                    'mediaEncryption': False, 'skype4b': False, 'h4601': True, 'h239': True,
                                    'h224': False, 'crypto': True, 'defaultResolution': '720p', 'ignore': False,
                                    'allowGroupCall': False, 'interpreter': False, 'privateAudioChannel': 10,
                                    'serveGateway': 'auto',
                                    'protectRTP': True, 'panasonicFEC': False}, 'avatar': None,
                               'status': {'connected': False, 'address': ''}}}
    with allure.step('Удаление аккаунта'):
        AccountsApi().delete_account(number)
    assert response['data'] == default_acc,\
        f"Настройки аккаунта отличаются от эталона {number}"


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта H323 и сравнение с дефолтными настройками response = 201')
def test_created_account_compare_with_default_h323_201(number):
    number = number
    with allure.step('Выполняем запрос на создание аккаунта и сравниваем с эталоном'):
        response = BaseApi().api_test('post', 'api/v1/accounts', number=number, type="H323", password='123').json()
    default_acc = {'account': {'addressBookContact': None, 'description': str(number), 'number': str(number),
                               'type': "H323", 'password': '123', 'email': '', 'source': 'local', 'tenant': None,
                               'group': None, 'groups': [], 'settings':
                                   {'bandwidth': 1536, 'resolutionP2P': '720p', 'behindNat': 'no', 'ip': 'dynamic',
                                    'port': 1720, 'transport': 'TCP', 'insecure': 'port', 'qualify': True,
                                    'codecs': ['g7221', 'h264', 'h263'], 'h264HighProfile': False,
                                    'h239sendContentInMainStream': False, 'mediaStreams': False, 'dtmf': 'rfc2833',
                                    'bfcpType': 'UDP',
                                    'mediaEncryption': False, 'skype4b': False, 'h4601': True, 'h239': True,
                                    'h224': False, 'crypto': True, 'defaultResolution': '720p', 'ignore': False,
                                    'allowGroupCall': False, 'interpreter': False, 'privateAudioChannel': 10,
                                    'serveGateway': 'auto',
                                    'protectRTP': True, 'panasonicFEC': False}, 'avatar': None,
                               'status': {'address': '0.0.0.0', 'connected': False}}}
    with allure.step('Удаление аккаунта'):
        AccountsApi().delete_account(number)
    assert response['data'] == default_acc,\
        f"Настройки аккаунта отличаются от эталона {number}"


@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Создание аккаунта WS и сравнение с дефолтными настройками response = 201')
def test_created_account_compare_with_default_ws_201(number):
    number = number
    with allure.step('Выполняем запрос на создание аккаунта и сравниваем с эталоном'):
        response = BaseApi().api_test('post', 'api/v1/accounts', number=number, type="WS", password='123').json()
    default_acc = {'account': {'addressBookContact': None, 'description': str(number), 'number': str(number),
                               'type': "WS", 'password': '123', 'email': '', 'source': 'local', 'tenant': None,
                               'group': None, 'groups': [], 'settings':
                                   {'bandwidth': 1536, 'resolutionP2P': '720p', 'behindNat': 'no', 'ip': 'dynamic',
                                    'port': 5060, 'transport': 'UDP', 'insecure': 'port', 'qualify': True,
                                    'codecs': ['opus', 'h264', 'vp8'], 'h264HighProfile': False,
                                    'h239sendContentInMainStream': False, 'mediaStreams': False, 'dtmf': 'rfc2833',
                                    'bfcpType': 'UDP',
                                    'mediaEncryption': False, 'skype4b': False, 'h4601': True, 'h239': True,
                                    'h224': False, 'crypto': True, 'defaultResolution': '720p', 'ignore': False,
                                    'allowGroupCall': False, 'interpreter': False, 'privateAudioChannel': 10,
                                    'serveGateway': 'auto',
                                    'protectRTP': True, 'panasonicFEC': False}, 'avatar': None,
                               'status': {'connected': False, 'address': ''}}}
    with allure.step('Удаление аккаунта'):
        AccountsApi().delete_account(number)
    assert response['data'] == default_acc,\
        f"Настройки аккаунта отличаются от эталона {number}"

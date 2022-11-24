import allure
import pytest
from api import *


@allure.id("12605")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Изменение всех настроек аккаунта')
@pytest.mark.parametrize('test_data', [
    ['description', 'test', 200],
    ['description', generate_random_string(130), 200],
    ['description', 'русский', 200],
    ['description', 'test с пробелами', 200],
    ['description', True, 422],
    ['description', generate_random_string(131), 422],
    ['description', '', 422],

    ['password', '123', 200],
    ['password', generate_random_string(10), 200],
    ['password', generate_random_string(1), 422],
    ['password', True, 422],

    ['email', 'test@email.com', 200],
    ['email', True, 422],
    ['email', 123, 422],

    ['bandwidth', 256, 200],
    ['bandwidth', 320, 200],
    ['bandwidth', 384, 200],
    ['bandwidth', 512, 200],
    ['bandwidth', 768, 200],
    ['bandwidth', 1024, 200],
    ['bandwidth', 1536, 200],
    ['bandwidth', 2048, 200],
    ['bandwidth', 2560, 200],
    ['bandwidth', 3072, 200],
    ['bandwidth', 3584, 200],
    ['bandwidth', 4096, 200],
    ['bandwidth', 4608, 200],
    ['bandwidth', 5120, 200],
    ['bandwidth', 5632, 200],
    ['bandwidth', 6144, 200],
    ['bandwidth', '256', 200],
    ['bandwidth', True, 422],
    ['bandwidth', 10000, 422],

    ['resolutionP2P', 'CIF', 200],
    ['resolutionP2P', '4CIF', 200],
    ['resolutionP2P', '640x360', 200],
    ['resolutionP2P', '720p', 200],
    ['resolutionP2P', 'FULLHD', 200],
    ['resolutionP2P', 720, 422],
    ['resolutionP2P', True, 422],

    ['mediaStreams', True, 200],
    ['mediaStreams', False, 200],
    ['mediaStreams', 123, 422],
    ['mediaStreams', 'fdsafds', 422],

    ['behindNat', 'no', 200],
    ['behindNat', 'yes', 200],
    ['behindNat', 'never', 200],
    ['behindNat', 123, 422],
    ['behindNat', 'fdsaf', 422],

    ['h264HighProfile', True, 200],
    ['h264HighProfile', False, 200],
    ['h264HighProfile', 123, 422],
    ['h264HighProfile', 'fdsaf', 422],

    ['qualify', True, 200],
    ['qualify', False, 200],
    ['qualify', 123, 422],
    ['qualify', 'fdsaf', 422],

    ['mediaEncryption', True, 200],
    ['mediaEncryption', False, 200],
    ['mediaEncryption', 123, 422],
    ['mediaEncryption', 'fdsaf', 422],

    ['skype4b', True, 200],
    ['skype4b', False, 200],
    ['skype4b', 123, 422],
    ['skype4b', 'fdsaf', 422],

    ['ip', '10.1.0.11', 200],
    ['ip', True, 422],
    ['ip', 123213, 422],

    ['port', 5070, 200],
    ['port', '5070', 200],
    ['port', True, 422],

    ['transport', 'UDP', 200],
    ['transport', 'TCP', 200],
    ['transport', generate_random_string(7), 422],
    ['transport', True, 422],
    ['transport', 123213, 422],

    ['insecure', 'port', 200],
    ['insecure', 'invite', 200],
    ['insecure', 'very', 200],
    ['insecure', generate_random_string(3), 422],
    ['insecure', True, 422],
    ['insecure', 123213, 422],

    ['bfcpType', 'UDP', 200],
    ['bfcpType', 'TCP', 200],
    ['bfcpType', generate_random_string(3), 422],
    ['bfcpType', True, 422],
    ['bfcpType', 123213, 422],

    ['dtmf', 'rfc2833', 200],
    ['dtmf', 'auto', 200],
    ['dtmf', 'inband', 200],
    ['dtmf', 'info', 200],
    ['dtmf', generate_random_string(10), 422],
    ['dtmf', True, 422],
    ['dtmf', 123213, 422],

    ['codecs', ['g7221', 'ulaw', 'h265', 'h264'], 200],
    ['codecs', False, 422],
    ['codecs', "['g7221','ulaw','h265','h264']", 422],

    ['defaultResolution', '128x72', 200],
    ['defaultResolution', '256x144', 200],
    ['defaultResolution', '320x180', 200],
    ['defaultResolution', '384x216', 200],
    ['defaultResolution', '512x288', 200],
    ['defaultResolution', '640x360', 200],
    ['defaultResolution', '768x432', 200],
    ['defaultResolution', '1024x576', 200],
    ['defaultResolution', '1152x648', 200],
    ['defaultResolution', '1408x792', 200],
    ['defaultResolution', '1536x864', 200],
    ['defaultResolution', '1664x936', 200],
    ['defaultResolution', '1792x1008', 200],
    ['defaultResolution', 'QSIF', 200],
    ['defaultResolution', 'QCIF', 200],
    ['defaultResolution', 'SIF', 200],
    ['defaultResolution', 'CIF', 200],
    ['defaultResolution', 'VGA', 200],
    ['defaultResolution', '4SIF', 200],
    ['defaultResolution', '4CIF', 200],
    ['defaultResolution', '480p', 200],
    ['defaultResolution', '576p', 200],
    ['defaultResolution', 'PAL', 200],
    ['defaultResolution', 'SVGA', 200],
    ['defaultResolution', 'XGA', 200],
    ['defaultResolution', '720p', 200],
    ['defaultResolution', '16CIF', 200],
    ['defaultResolution', 'FULLHD', 200],
    ['defaultResolution', 'UHD', 200],
    ['defaultResolution', True, 422],
    ['defaultResolution', ['UHD', 123], 422],

    ['ignore', True, 200],
    ['ignore', False, 200],
    ['ignore', 123, 422],
    ['ignore', 'fdsaf', 422],

    ['interpreter', True, 200],
    ['interpreter', False, 200],
    ['interpreter', 123, 422],
    ['interpreter', 'fdsaf', 422],

    ['protectRTP', True, 200],
    ['protectRTP', False, 200],
    ['protectRTP', 123, 422],
    ['protectRTP', 'fdsaf', 422]
])
def test_accounts_change_settings(created_accounts, test_data):
    account = created_accounts[0]
    param, value, rez = test_data
    with allure.step('Выполняем запрос на изменение настроек аккаунта'):
        response = BaseApi().call_method('patch', f'api/v1/account/{account}', data={param: value, 'type': 'SIP'})
    assert_expected_result(response, param, value, rez)


@allure.id("12603")
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


@allure.id("12604")
@allure.feature('API')
@allure.story('API ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'api')
@allure.title('Изменение настроек несуществующего аккаунта response = 404')
def test_accounts_change_settings_404(created_accounts):
    with allure.step('Выполняем запрос на изменение настроек несуществующего аккаунта --- 8793249832'):
        response = BaseApi().call_method('patch', f'api/v1/account/8793249832', data={'description': 'test'})
    assert response.status_code == 404, f"Ответ сервера отличается от ожидаемого response = {response.json()}"


@allure.id("12605")
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

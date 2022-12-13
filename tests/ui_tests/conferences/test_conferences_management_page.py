from model.pages import *
from selene.support.shared import browser
from api import *
import pytest


@pytest.fixture()
def participant():
    number = str(acc_num_generation())
    Api().create_account(number=number, description=generate_random_string(10))
    yield number
    Api().delete_account(number)


@pytest.fixture()
def management():
    number = str(conf_num_generation())
    Api().create_conference(description='Поиск конференции', number=number)
    yield number
    Api().delete_conference(number)


@allure.feature('UI')
@allure.story('UI ALL')
@allure.suite('Конференции')
@allure.tag('autotests', 'ui')
@allure.title('Запуск конференции')
@pytest.mark.parametrize('call_all', [True, False])
def test_start_conference(management, call_all):
    auth()
    open_conference_management_page(management)
    start_conference(call_all=call_all)
    # browser.save_screenshot('./screenshots/conferences/')
    assert get_value(Api().get_conferences_list(search=management), 'active'), \
        "Конференция не запущена"


@allure.feature('UI')
@allure.story('UI ALL')
@allure.suite('Конференции')
@allure.tag('autotests', 'ui')
@allure.title('Добавить участника конференции')
def test_add_participant(management, participant):
    auth()
    open_conference_management_page(management)
    add_participant(participant)
    # browser.save_screenshot('./screenshots/conferences/')
    assert get_value(Api().get_conferences_list(search=management), 'total') > 0, \
        """Список участников конференции пуст, участник не добавлен в конференцию"""


@pytest.fixture()
def fast_call_in_conference(management):
    Api().create_conference(number=management, 
                            description='fast_call_test')
    Api().start_conference(management)
    yield management
    Api().delete_conference(management)


@allure.feature('UI')
@allure.story('UI ALL')
@allure.suite('Конференции')
@allure.tag('autotests', 'ui')
@allure.title('Быстрый вызов анонимного участника в конференцию')
@pytest.mark.parametrize('types', ['SIP', 'H323'])
@pytest.mark.parametrize('resolutions', ['720p', 'CIF'])
@pytest.mark.parametrize('fps', ['25', '15'])
@pytest.mark.parametrize('speed', ['512', '320'])
def test_fast_call(fast_call_in_conference, types, resolutions, fps, speed):
    auth()
    open_conference_management_page(fast_call_in_conference)
    fast_call(number=TestData.second_ip, type=types, resolution=resolutions, fps=fps, speed=speed)
    # browser.save_screenshot('./screenshots/conferences/')
    assert get_value(Api().get_conferences_list(search=fast_call_in_conference), 'online') > 0, \
        """Список подключенных участников конференции пуст,
         быстрый вызов не выполнен"""

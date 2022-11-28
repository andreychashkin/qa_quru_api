from model.pages import *
from selene.support.shared import browser
from api import *
import pytest


@pytest.fixture()
def participant(open_server):
    number = str(acc_num_generation())
    Api().create_account(number=number, description=generate_random_string(10))
    yield number
    Api().delete_account(number)


@pytest.fixture()
def management(open_server):
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
    browser.save_screenshot('./screenshots/conferences/')
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
    assert get_value(Api().get_conferences_list(search=management), 'total') > 0, \
        """Список участников конференции пуст, участник не добавлен в конференцию"""

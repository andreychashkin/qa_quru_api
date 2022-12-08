from model.pages import *
from api import *
import pytest


@pytest.fixture()
def conference_number():
    conference_number = conf_num_generation()
    yield conference_number
    Api().delete_conference(conference_number)


@allure.feature('UI')
@allure.story('UI ALL')
@allure.suite('Конференции')
@allure.tag('autotests', 'ui')
@allure.title('Создание конференции')
@pytest.mark.parametrize('description', [generate_random_string(3),
                                         generate_random_string(10),
                                         generate_random_string(30)])
def test_created_conference_description(conference_number, description):
    auth()
    open_conferences_page()
    open_the_conference_creation_window()
    fill_form_conference_fields(number=conference_number,
                                description=description)
    browser.save_screenshot('./screenshots/conferences/')
    assert len(
        get_value(
            Api().get_conferences_list(search=conference_number), 'conferences'
            )
    ) > 0, 'Созданная конференция отсутствует в списке конференций сервера'


@pytest.fixture()
def search_conference():
    number = str(conf_num_generation())
    Api().create_conference(description='Поиск конференции', number=number)
    yield number
    Api().delete_conference(number)


@allure.feature('UI')
@allure.story('UI ALL')
@allure.suite('Конференции')
@allure.tag('autotests', 'ui')
@allure.title('Поиск конференции и переход к странице управления ею')
def test_search_and_open_conference(search_conference):
    auth()
    open_conferences_page()
    type_to_search_confernece(search_conference)
    search_conference_in_table(search_conference, open=True)
    browser.save_screenshot('./screenshots/conferences/')
    assert search_conference in browser.driver.current_url, \
        'Url не вляется адресом страницы конференции'

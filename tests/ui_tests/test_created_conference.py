from model.pages import *
from selene.support.shared import browser
from api import *
import pytest


@pytest.fixture()
def conference_number():
    conference_number = conf_num_generation()
    yield conference_number
    Api().delete_conference(conference_number)


@pytest.mark.parametrize('description', [generate_random_string(3),
                                         generate_random_string(10),
                                         generate_random_string(30)])
def test_created_conference_description(open_server, description, conference_number):
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

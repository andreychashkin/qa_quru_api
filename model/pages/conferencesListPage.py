from selene.support.shared import browser
from api import *
import allure
import time


def open_conferences_page():
    """Переход на страницу со списком конференций"""
    with allure.step('Переход на страницу списка конференций'):
        browser.open('/conferences')


def open_the_conference_creation_window():
    """Открыть окно создания конференции"""
    with allure.step('Открываем окно создания конференции'):
        browser.element('[data-target="#modal_add"]').click()


def fill_form_conference_fields(number: str,
                                description: str,
                                moderators: list = None):
    """Заполняем форму создания конференции"""
    with allure.step('Заполняем форму создания конференции'):
        browser.element('#conference_add_number').clear().type(number)
        browser.element('form  [name=description]').type(description)
        if moderators:
            for number in moderators:
                browser.element('#account-search-select-component input[type=text]').type(number)
                browser.element('#account-search-select-component  span i').click()
        browser.element('#account-search-select-component')
        browser.element('form[name=add] button[type=submit]').click()
        time.sleep(1)

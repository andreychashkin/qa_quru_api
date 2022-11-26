from selene.support.shared import browser
from api import *
import allure
import time


def open_the_account_creation_form():
    """Открываем окно создания абонента/аккаунта на сервере"""
    with allure.step('Создаем нового абонента на сервере'):
        browser.element('*[href="#/accounts/add"]').click()


def fill_creation_account_form(type_acc: str,
                               description: str,
                               bandwidth: str,
                               password: str = TestData.password,
                               number: str = None
                               ):
    """Заполняем обязательные поля формы создания аккаунта/абонента"""
    with allure.step('Заполняем форму и жмем Добавать'):
        browser.element('select[name=type]').send_keys(type_acc)
        browser.element('input[name=description]').type(description)
        if number:
            browser.element('input[name=number]').clear().type(number)
        browser.element('input[name=password]').clear().type(password)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        browser.element('select[name=bandwidth]').send_keys(bandwidth)
        browser.element('*[form=form-2]').click()
        time.sleep(1)


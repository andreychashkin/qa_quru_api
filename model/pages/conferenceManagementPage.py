from selene.support.shared import browser
from selene import by, be, have
from api import *
import allure
import time


def open_conference_management_page(conference_number: str) -> None:
    """Открываем страницу управления конференции"""
    with allure.step("Переходим на страницу управления конференцией"):
        browser.open(f'/conferences/control/{conference_number}')
        

def start_conference(call_all: bool = False) -> None:
    """Клик на кнопку старта конференции и подтверждение в окне"""
    with allure.step("Запускаем конференцию"):
        browser.element('#run').click()
        if call_all:
            with allure.step("Чекбокс вызвать всех"):
                browser.element('[name=run] .btn-slider').click()
        browser.element('[name=run] [type=submit]').click()


def add_participant(number: str) -> None:
    """Добавляем участника конференции"""
    with allure.step("Добавляем участника конференции"):
        browser.element("#nav-control [data-target='#modal_fastadd']").click()
        browser.element("#conference-fast-add-participants-account-select [type=text]").type(number)
        browser.element(f"//*[text()='{number}']").click()
        browser.element('#fakesubmit[name=submit]').should(be.clickable).click()

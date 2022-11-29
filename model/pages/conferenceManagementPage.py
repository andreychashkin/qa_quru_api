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
        time.sleep(1)


def add_participant(number: str) -> None:
    """Добавляем участника конференции"""
    with allure.step("Добавляем участника конференции"):
        browser.element("#nav-control [data-target='#modal_fastadd']").click()
        browser.element("#conference-fast-add-participants-account-select [type=text]").type(number)
        browser.element(f"//*[text()='{number}']").click()
        browser.element('#fakesubmit[name=submit]').should(be.clickable).click()
        time.sleep(1)


def fast_call(number: str, 
              type: str = None,
              resolution: str = None,
              fps: str = None,
              speed: str = None):
    """Выполняем быстрый вызов в конференцию. 
    Без указания параметров используются базовые"""
    with allure.step("Открываем окно быстрого вызова"):
        browser.element("[data-target='#modal_call']").click()
    with allure.step("Указываем параметры вызова"):
        browser.element('[name=number]').type(number)
        if type:
            browser.element('#wraper #callTypeBtn').click()
            browser.element(f'li a[data-type={type}]').click()
        if resolution:
            browser.element('[name=resolution]').type(resolution)
        if fps:
            browser.element('[name=fps]').type(fps)
        if speed:
            browser.element('[name=speed]').type(speed)
    with allure.step("Выполняем вызов"):
        browser.element('#submitCall').click()
        time.sleep(4)

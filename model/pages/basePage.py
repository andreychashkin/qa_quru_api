from selene.support.shared import browser
from selene import by, be, have
from api import *
import allure
import time


def go_main_page():
    with allure.step('Переходим на главную страницу'):
        return browser.open('/main')


def go_acounts_page():
    with allure.step('Переходим на страницу Абонентов'):
        return browser.open('/accounts#')

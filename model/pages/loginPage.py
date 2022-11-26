from selene.support.shared import browser
from selene import by, be, have
from api import *
import allure
import time


def auth(login=TestData.login, password=TestData.password):
    with allure.step('Авторизуемся на сервере'):
        browser.element('#loginForm [name="username"]').type(login)
        browser.element('#loginForm [name="password"]').type(password)
        browser.element('#loginForm [type="submit"]').click()

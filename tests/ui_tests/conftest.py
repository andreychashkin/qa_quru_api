import pytest
from selene.support.shared import browser
from api import *


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = f'https://{TestData.ip_server}'
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    yield


@pytest.fixture()
def open_and_quit_browser_automation_practice_form():
    browser.open('/')
    yield
    browser.quit()

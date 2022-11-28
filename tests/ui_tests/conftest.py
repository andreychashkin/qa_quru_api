import pytest
from selene.support.shared import browser
from api import *
import time


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = f'https://demo.vinteo.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1024
    yield


@pytest.fixture()
def open_server():
    browser.open('/')
    yield
    browser.quit()

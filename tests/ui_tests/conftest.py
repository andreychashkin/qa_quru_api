import pytest
from selene.support.shared import browser
# from pyvirtualdisplay import Display
from api import *

# display = Display(visible=False, size=(1920, 1100))
# display.start()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = f'https://demo.vinteo.com'
    browser.config.browser_name = TestData.selene_browser
    browser.config.window_width = 1920
    browser.config.window_height = 1024
    yield


@pytest.fixture()
def open_server():
    browser.open('/')
    yield
    browser.quit()

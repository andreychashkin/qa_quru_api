import pytest
from selene.support.shared import browser
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1200, 1200))
display.start()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = f'https://demo.vinteo.com'
    browser.config.browser_name = 'firefox'
    browser.config.window_width = 1100
    browser.config.window_height = 1024
    yield


@pytest.fixture()
def open_server():
    browser.open('/')
    yield
    browser.quit()

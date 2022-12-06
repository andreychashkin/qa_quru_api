import time

import pytest
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from model.utils import attach
from selene.support.shared import browser
# from pyvirtualdisplay import Display
from api import *
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup():
    options = Options()
    selenoid_capabilities = {
        "browserName": TestData.selene_browser,
        "browserVersion": TestData.selene_browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{TestData.selenoid_login}:{TestData.selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.base_url = f'https://demo.vinteo.com'
    browser.config.window_width = 1920
    browser.config.window_height = 900
    browser.open('/')
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


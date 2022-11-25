from model.pages import *
from selene.support.shared import browser
import pytest
import time


def test_created_account(open_and_quit_browser_automation_practice_form):
    auth()
    time.sleep(5)
    browser.save_screenshot('./screenshots/')
from model.pages import *
from selene.support.shared import browser
from api import *
import pytest


@pytest.fixture()
def account_number():
    number = acc_num_generation()
    yield number
    Api().delete_account(number)


@allure.feature('UI')
@allure.story('UI ALL')
@allure.suite('Аккаунты')
@allure.tag('autotests', 'ui')
@allure.title('Создание аккаунта')
@pytest.mark.parametrize('types_account', ['SIP', 'H323', 'WS'])
@pytest.mark.parametrize('bandwidth', ['512', '1536', '4096', '6144'])
def test_created_accoun(open_server, account_number, types_account, bandwidth):
    auth()
    go_acounts_page()
    open_the_account_creation_form()
    fill_creation_account_form(type_acc=types_account,
                               number=account_number,
                               description='test-description',
                               bandwidth=bandwidth)
    browser.save_screenshot('./screenshots/accounts/')
    assert get_value(Api().get_accounts_list(search=account_number), 'total') > 0, \
        'Созданный аккаунт отсутствует в списке абонентов сервера'

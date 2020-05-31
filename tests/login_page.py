import pytest
from selenium.common.exceptions import TimeoutException


def test_login_page(account):
    try:
        account.find_element(account.driver, account.list_group)
        account.find_element(account.driver, account.button_Continue)
        account.find_element(account.driver, account.container_account_login)
        account.find_element(account.driver, account.navbar_header)
        account.find_element(account.driver, account.link_Forgotten_Password)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента')

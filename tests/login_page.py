import pytest
from locators import Locators
from selenium.common.exceptions import TimeoutException


def test_login_page(account):
    try:
        account.find_element(account.driver, Locators.list_group)
        account.find_element(account.driver, Locators.button_Continue)
        account.find_element(account.driver, Locators.container_account_login)
        account.find_element(account.driver, Locators.navbar_header)
        account.find_element(account.driver, Locators.link_Forgotten_Password)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента')

import pytest
from locators import Locators
from selenium.common.exceptions import TimeoutException


def test_admin_login(admin):
    try:
        admin.find_element(admin.driver, Locators.input_username)
        admin.find_element(admin.driver, Locators.input_password)
        admin.find_element(admin.driver, Locators.footer)
        admin.find_element(admin.driver, Locators.panel_title)
        admin.find_element(admin.driver, Locators.link_OpenCart)
        print('\nВсе элементы найдены')
    except TimeoutException :
        pytest.fail('\nНе дождался элемента')

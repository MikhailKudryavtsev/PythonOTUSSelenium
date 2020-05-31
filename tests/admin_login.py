import pytest
from selenium.common.exceptions import TimeoutException


def test_admin_login(admin):
    try:
        admin.find_element(admin.driver, admin.input_username)
        admin.find_element(admin.driver, admin.input_password)
        admin.find_element(admin.driver, admin.footer)
        admin.find_element(admin.driver, admin.panel_title)
        admin.find_element(admin.driver, admin.link_OpenCart)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail('\nНе дождался элемента')

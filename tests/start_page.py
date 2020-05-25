import pytest
from selenium.common.exceptions import TimeoutException
from locators import Locators


def test_start_page(start_page):
    try:
        start_page.find_element(start_page.driver, Locators.your_store)
        start_page.find_element(start_page.driver, Locators.button_cart)
        start_page.find_element(start_page.driver, Locators.form_currency)
        start_page.find_element(start_page.driver, Locators.list_buttons)
        start_page.find_element(start_page.driver, Locators.link_MacBook)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента')

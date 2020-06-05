import pytest
from selenium.common.exceptions import TimeoutException


def test_start_page(start_page):
    try:
        start_page.find_element(start_page.driver, start_page.your_store)
        start_page.find_element(start_page.driver, start_page.button_cart)
        start_page.find_element(start_page.driver, start_page.form_currency)
        start_page.find_element(start_page.driver, start_page.list_buttons)
        start_page.find_element(start_page.driver, start_page.link_MacBook)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента')

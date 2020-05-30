import pytest
from locators import Locators
from selenium.common.exceptions import TimeoutException


def test_product_id(product):
    product.get_url()
    try:
        product.find_element(product.driver, Locators.h1_device_name)
        product.find_element(product.driver, Locators.button_add_card)
        product.find_element(product.driver, Locators.container_product)
        product.find_element(product.driver, Locators.nav_tabs)
        product.find_element(product.driver, Locators.link_OpenCart)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента')

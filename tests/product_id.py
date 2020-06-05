import pytest
from selenium.common.exceptions import TimeoutException


def test_product_id(product):
    product.get_url()
    try:
        product.find_element(product.driver, product.h1_device_name)
        product.find_element(product.driver, product.button_add_card)
        product.find_element(product.driver, product.container_product)
        product.find_element(product.driver, product.nav_tabs)
        product.find_element(product.driver, product.link_OpenCart)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента')

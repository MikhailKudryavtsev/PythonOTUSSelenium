import pytest
from locators import Locators
from selenium.common.exceptions import TimeoutException


def test_check_table_products(product):
    product.open_products()
    try:
        product.find_element(product.driver, Locators.form_product)
        print('\nПоявилась таблица с товарами')
    except TimeoutException:
        pytest.fail('\nТаблица с товарами не появилась за 15 секунд ожидания.')

import pytest
from selenium.common.exceptions import NoSuchElementException


def test_add_product(product):
    product.create_product()
    try:
        product.driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.random_name}")]')
        print(f'\nТовар "{product.random_name}" добавлен')
    except NoSuchElementException:
        pytest.fail('\nТовар не добавлен')

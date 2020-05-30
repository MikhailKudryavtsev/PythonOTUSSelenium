import pytest
from selenium.common.exceptions import NoSuchElementException


def test_remove_product(product):
    product.remove_product()
    try:
        product.driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.random_name}")]')
        pytest.fail(f'\nТовар "{product.random_name}" не удален')
    except NoSuchElementException:
        print(f'\nТовар "{product.random_name}" удален')

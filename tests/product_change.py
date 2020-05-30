import pytest
from selenium.common.exceptions import NoSuchElementException


def test_product_change(product):
    product.product_change()
    try:
        product.driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.new_name}")]')
        print(f'\nТовар "{product.old_name}" был переименован в "{product.new_name}"')
    except NoSuchElementException:
        pytest.fail('\nТовар не был переименован')

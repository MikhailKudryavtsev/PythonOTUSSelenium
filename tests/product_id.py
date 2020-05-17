import pytest
from selenium.common.exceptions import NoSuchElementException


def test_product_id(url, driver):
    driver.get(f'{url}index.php?route=product/product&path=57&product_id=49')
    try:
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/h1')
        driver.find_element_by_css_selector('button#button-cart')
        driver.find_element_by_id('product-product')
        driver.find_element_by_class_name('form-horizontal')
        driver.find_element_by_link_text('OpenCart')
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')

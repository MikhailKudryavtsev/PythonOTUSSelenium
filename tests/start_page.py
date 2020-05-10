import pytest
from selenium.common.exceptions import NoSuchElementException


def test_start_page(url, driver):
    driver.get(url)
    try:
        driver.find_element_by_xpath('//*[@id="logo"]/h1/a')
        driver.find_element_by_css_selector('.btn-group.btn-block')
        driver.find_element_by_id('form-currency')
        driver.find_element_by_class_name('list-inline')
        driver.find_element_by_link_text('MacBook')
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')


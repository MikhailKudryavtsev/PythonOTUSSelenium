import pytest
from selenium.common.exceptions import NoSuchElementException


def test_admin_login(url, driver):
    driver.get(f'{url}admin/')
    try:
        driver.find_element_by_xpath('//*[@id="input-username"]')
        driver.find_element_by_css_selector('input#input-username')
        driver.find_element_by_id('footer')
        driver.find_element_by_class_name('panel-title')
        driver.find_element_by_link_text('OpenCart')
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')

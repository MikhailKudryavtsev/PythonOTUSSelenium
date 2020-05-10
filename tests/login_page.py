import pytest
from selenium.common.exceptions import NoSuchElementException


def test_login_page(url, driver):
    driver.get(f'{url}index.php?route=account/login')
    try:
        driver.find_element_by_xpath('//*[@id="column-right"]/div')
        driver.find_element_by_css_selector('a.btn.btn-primary')
        driver.find_element_by_id('account-login')
        driver.find_element_by_class_name('navbar-header')
        driver.find_element_by_link_text('Forgotten Password')
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')

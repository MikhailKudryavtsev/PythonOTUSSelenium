import pytest
from selenium.common.exceptions import NoSuchElementException


def test_category_page(url, driver):
    driver.get(f'{url}index.php?route=product/category&path=20')
    try:
        driver.find_element_by_xpath('//*[@id="search"]/span/button')
        driver.find_element_by_css_selector('ul.nav.navbar-nav')
        driver.find_element_by_id('column-left')
        driver.find_element_by_class_name('swiper-viewport')
        driver.find_element_by_link_text('Desktops')
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')

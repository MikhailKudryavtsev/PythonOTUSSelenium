import pytest
from locators import Locators
from selenium.common.exceptions import TimeoutException


def test_category_page(category):
    try:
        category.find_element(category.driver, Locators.button_search)
        category.find_element(category.driver, Locators.navbar)
        category.find_element(category.driver, Locators.left_column)
        category.find_element(category.driver, Locators.swiper_viewport)
        category.find_element(category.driver, Locators.link_Desktops)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail('\nНе дождался элемента')

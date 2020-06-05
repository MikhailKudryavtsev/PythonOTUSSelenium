import pytest
from selenium.common.exceptions import TimeoutException


def test_category_page(category):
    try:
        category.find_element(category.driver, category.button_search)
        category.find_element(category.driver, category.navbar)
        category.find_element(category.driver, category.left_column)
        category.find_element(category.driver, category.swiper_viewport)
        category.find_element(category.driver, category.link_Desktops)
        print('\nВсе элементы найдены')
    except TimeoutException:
        pytest.fail('\nНе дождался элемента')

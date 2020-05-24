import pytest
from my_wait import MyVisibilityOfSelector
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

def test_admin_login(url, driver):
    driver.get(f'{url}admin/')
    try:
        selector = '//*[@id="input-username"]'
        MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
        driver.find_element_by_xpath(selector)

        selector = 'input#input-username'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector)

        selector = 'footer'
        MyVisibilityOfSelector(driver, By.ID, selector).wdw()
        driver.find_element_by_id(selector)

        selector = 'panel-title'
        MyVisibilityOfSelector(driver, By.CLASS_NAME, selector).wdw()
        driver.find_element_by_class_name(selector)

        selector = 'OpenCart'
        MyVisibilityOfSelector(driver, By.LINK_TEXT, selector).wdw()
        driver.find_element_by_link_text(selector)
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента - {selector}')

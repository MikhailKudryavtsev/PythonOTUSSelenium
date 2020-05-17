import pytest
from my_wait import MyVisibilityOfSelector
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


def test_login_page(url, driver):
    driver.get(f'{url}index.php?route=account/login')
    try:
        selector = '//*[@id="column-right"]/div'
        MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
        driver.find_element_by_xpath(selector)

        selector = 'a.btn.btn-primary'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector)

        selector = 'account-login'
        MyVisibilityOfSelector(driver, By.ID, selector).wdw()
        driver.find_element_by_id(selector)

        selector = 'navbar-header'
        MyVisibilityOfSelector(driver, By.CLASS_NAME, selector).wdw()
        driver.find_element_by_class_name(selector)

        selector = 'Forgotten Password'
        MyVisibilityOfSelector(driver, By.LINK_TEXT, selector).wdw()
        driver.find_element_by_link_text(selector)
        print('\nВсе элементы найдены')
    except NoSuchElementException as e:
        pytest.fail(f'\nНет элемента - {e}')
    except TimeoutException:
        pytest.fail(f'\nНе дождался элемента - {selector}')

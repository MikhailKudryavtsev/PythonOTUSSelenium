import pytest
from my_wait import MyVisibilityOfSelector
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

def test_product_id(url, driver):
    driver.get(f'{url}index.php?route=product/product&path=57&product_id=49')
    try:
        selector = '//*[@id="content"]/div/div[2]/h1'
        MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
        driver.find_element_by_xpath(selector)

        selector = 'button#button-cart'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector)

        selector = 'product-product'
        MyVisibilityOfSelector(driver, By.ID, selector).wdw()
        driver.find_element_by_id(selector)

        selector = 'nav-tabs'
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
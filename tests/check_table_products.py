
import pytest
from my_wait import MyVisibilityOfSelector
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def test_check_table_products(url, driver):
    driver.get(f'{url}admin/')
    selector = 'input#input-username'
    MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
    driver.find_element_by_css_selector(selector).send_keys('user')
    selector = 'input#input-password'
    MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
    driver.find_element_by_css_selector(selector).send_keys('bitnami1')
    driver.find_element_by_css_selector('button.btn.btn-primary').click()
    selector = '//*[@id="menu-catalog"]/a'
    MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
    driver.find_element_by_xpath(selector).click()
    selector = '//*[@id="collapse1"]/li[2]/a'
    MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
    driver.find_element_by_xpath(selector).click()
    try:
        selector = 'form#form-product'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        print('\nПоявилась таблица с товарами')
    except TimeoutException:
        pytest.fail('\nТаблица с товарами не появилась за 5 секунд ожидания.')



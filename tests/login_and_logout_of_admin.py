
import pytest
from my_wait import MyVisibilityOfSelector
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def test_login_and_logout_of_admin(url, driver):
    driver.get(f'{url}admin/')
    selector = 'input#input-username'
    MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
    driver.find_element_by_css_selector(selector).send_keys('user')
    selector = 'input#input-password'
    MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
    driver.find_element_by_css_selector(selector).send_keys('bitnami1')
    driver.find_element_by_css_selector('button.btn.btn-primary').click()
    try:
        selector = 'img#user-profile.img-circle'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        print('\nПроизошла авторизация')
        try:
            driver.find_element_by_xpath('//*[@id="header"]/div/ul/li[2]/a').click()
            selector = 'h1.panel-title'
            MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
            print('\nПроизошел разлогин')
        except TimeoutException:
            pytest.fail(f'\nРазлогин не произошел, т.к. не дождался элемента - {selector}')
    except TimeoutException:
        pytest.fail(f'\nАвторизация не произошла, т.к. не дождался элемента - {selector}')

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from backstory import CreateProduct
from my_wait import MyVisibilityOfSelector


def test_remove_product(url, driver):
    product = CreateProduct()
    product.backstory(url, driver)
    selector = '//*[@id="form-product"]/div/table/tbody/tr'
    MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
    items = driver.find_elements_by_xpath(selector)
    for i in range(1, (len(items) + 1)):
        if product.random_name in driver.find_element_by_xpath(
                f'//*[@id="form-product"]/div/table/tbody/tr[{i}]').get_attribute('textContent'):
            driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr[{i}]/td[1]/input').click()
    driver.find_element_by_css_selector('button.btn.btn-danger').click()
    Alert(driver).accept()
    try:
        driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.random_name}")]')
        pytest.fail(f'\nТовар "{product.random_name}" не удален')
    except NoSuchElementException:
        print(f'\nТовар "{product.random_name}" удален')
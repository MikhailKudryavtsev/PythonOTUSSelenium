# import pytest
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.alert import Alert
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from backstory import CreateProduct
from my_wait import MyVisibilityOfSelector


def test_product_change(url, driver):
    product = CreateProduct()
    product.backstory(url, driver)
    selector = '//*[@id="form-product"]/div/table/tbody/tr'
    MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
    items = driver.find_elements_by_xpath(selector)
    for i in range(1, (len(items) + 1)):
        if product.random_name in driver.find_element_by_xpath(
                f'//*[@id="form-product"]/div/table/tbody/tr[{i}]').get_attribute('textContent'):
            driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr[{i}]/td[8]/a').click()
            break
    selector = 'input#input-name1'
    MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
    old_name = product.random_name
    product.create_name()
    new_name = product.random_name
    driver.find_element_by_css_selector(selector).clear()
    driver.find_element_by_css_selector(selector).send_keys(new_name)
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()
    selector = '//*[@id="form-product"]/div/table/tbody/tr'
    MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
    try:
        driver.find_element_by_xpath(f'//*/td[contains(text(), "{new_name}")]')
        print(f'\nТовар {old_name} был переименован в {new_name}')
    except NoSuchElementException:
        pytest.fail('\nТовар не был переименован')

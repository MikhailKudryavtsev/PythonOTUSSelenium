import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from backstory import CreateProduct
from my_wait import MyVisibilityOfSelector


def test_add_product(url, driver):
    product = CreateProduct()
    product.backstory(url, driver)
    selector = '//*[@id="form-product"]/div/table/tbody/tr'
    MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
    try:
        driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.random_name}")]')
        print(f'\nТовар "{product.random_name}" добавлен')
    except NoSuchElementException:
        pytest.fail('\nТовар не добавлен')

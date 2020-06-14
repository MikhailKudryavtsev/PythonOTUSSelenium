import allure
from selenium.common.exceptions import TimeoutException


@allure.title("Тест проверки таблицы продуктов")
def test_check_table_products(product):
    product.open_products()
    try:
        product.find_element(product.driver, product.form_product)
        print('\nПоявилась таблица с товарами')
    except TimeoutException as e:
        allure.attach(body=product.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)

import allure
from selenium.common.exceptions import NoSuchElementException


@allure.feature("Работа с продуктом")
@allure.story("Добавление продукта")
@allure.title('Тест добавления продукта')
def test_add_product(product):
    product.create_product()
    try:
        with allure.step("Поиск добавленного продукта"):
            product.driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.random_name}")]')
            print(f'\nТовар "{product.random_name}" добавлен')
    except NoSuchElementException as e:
        allure.attach(body=product.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)

@allure.feature("Работа с продуктом")
@allure.story("Удаление продукта")
@allure.title('Тест удаления продукта')
def test_remove_product(product):
    product.remove_product()
    try:
        with allure.step("Поиск удаленного продукта"):
            product.driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.random_name}")]')
            allure.attach(body=product.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError()
    except NoSuchElementException:
        print(f'\nТовар "{product.random_name}" удален')

@allure.feature("Работа с продуктом")
@allure.story("Изменение продукта")
@allure.title('Тест изменения продукта')
def test_product_change(product):
    product.product_change()
    try:
        with allure.step("Поиск измененного продукта"):
            product.driver.find_element_by_xpath(f'//*/td[contains(text(), "{product.new_name}")]')
            print(f'\nТовар "{product.old_name}" был переименован в "{product.new_name}"')
    except NoSuchElementException as e:
        allure.attach(body=product.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)

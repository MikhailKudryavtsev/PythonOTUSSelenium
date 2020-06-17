import allure

@allure.title("Тест проверки фильтра по имени")
def test_filter_by_name(product):
    product.create_product()
    product.filter()
    with allure.step("Поиск элементов"):
        item = product.find_element(product.driver, product.tbody_tr_td3)
    assert product.random_name == item.get_attribute('textContent'), 'Фильтр выдал не тот продукт'

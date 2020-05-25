
def test_filter_by_name(product):
    product.create_product()
    product.filter()
    item = product.driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr/td[1]')
    assert product.random_name == item.get_attribute('textContent'), 'Фильтр выдал не тот продукт'

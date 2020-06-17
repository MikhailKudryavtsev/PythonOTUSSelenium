import allure


@allure.title("Тест проверки поиска")
def test_check_search(start_page):
    with allure.step("Переход на url"):
        start_page.get_url()
    start_page.search()
    assert start_page.random_name in start_page.result.get_attribute('textContent'), 'Поиск выдал не тот результат'
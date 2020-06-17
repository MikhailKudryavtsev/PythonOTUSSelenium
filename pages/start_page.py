import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):

    button_cart = (By.CSS_SELECTOR, '.btn-group.btn-block')
    cart_dropdown_menu = (By.CSS_SELECTOR, 'ul.dropdown-menu.pull-right')
    input_search = (By.CSS_SELECTOR, 'input.form-control.input-lg')
    search_results = (By.CSS_SELECTOR, 'div.col-sm-12')
    form_currency = (By.ID, 'form-currency')
    list_buttons = (By.CLASS_NAME, 'list-inline')
    link_MacBook = (By.LINK_TEXT, 'MacBook')
    your_store = (By.XPATH, '//*[@id="logo"]/h1/a')

    def __init__(self, url, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = url

    def open_cart(self):
        self.browser_logs()
        self.proxy_logs()
        with allure.step("Открытие корзины"):
            self.find_element(self.driver, self.button_cart).click()
        self.logger.info(f'Clicked element: {self.button_cart}')
        with allure.step("Поиск элементов"):
            self.cart_menu = self.find_element(self.driver, self.cart_dropdown_menu)
        return self.cart_menu

    def get_url(self):
        return self.driver.get(self.url)

    def search(self):
        self.browser_logs()
        self.proxy_logs()
        self.create_name()
        with allure.step("Ввод названия продукта в строку поиска"):
            self.find_element(self.driver, self.input_search).send_keys(self.random_name)
        self.logger.info(f'Entered text "{self.random_name}" in {self.input_search}')
        self.find_element(self.driver, self.button_search).click()
        self.logger.info(f'Clicked element: {self.button_search}')
        with allure.step("Поиск введенного продукта"):
            self.result = self.find_element(self.driver, self.search_results)
        return self.result

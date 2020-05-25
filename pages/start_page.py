from locators import Locators
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, url, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = url

    def open_cart(self):
        self.find_element(self.driver, Locators.button_cart).click()
        self.cart_menu = self.find_element(self.driver, Locators.cart_dropdown_menu)
        return self.cart_menu

    def get_url(self):
        return self.driver.get(self.url)

    def search(self):
        self.create_name()
        self.find_element(self.driver, Locators.input_search).send_keys(self.random_name)
        self.find_element(self.driver,Locators.button_search).click()
        self.result = self.find_element(self.driver, Locators.search_results)
        return self.result

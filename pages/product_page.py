from selenium.webdriver.common.alert import Alert

from pages.base_page import BasePage
from pages.admin_page import AdminPage
from locators import Locators

class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_product(self):
        self.create_name()
        self.open_products()
        self.find_element(self.driver, Locators.button_add_product).click()
        self.find_element(self.driver, Locators.input_product_name).send_keys(self.random_name)
        self.find_element(self.driver, Locators.input_meta_title).send_keys('TestTagTitle')
        self.driver.find_element_by_link_text('Data').click()
        self.find_element(self.driver, Locators.input_model).send_keys('TestModel')
        self.find_element(self.driver, Locators.button_save_products).click()
        self.find_element(self.driver, Locators.tbody_tr_products)

    def open_products(self):
        admin_page = AdminPage(self.driver)
        admin_page.get_url()
        admin_page.authorization_admin()
        self.find_element(self.driver, Locators.catalog).click()
        self.find_element(self.driver, Locators.products).click()

    def product_change(self):
        self.create_product()
        items = self.find_elements(self.driver, Locators.tbody_tr_products)
        for i in range(1, (len(items) + 1)):
            if self.random_name in self.driver.find_element_by_xpath(
                    f'//*[@id="form-product"]/div/table/tbody/tr[{i}]').get_attribute('textContent'):
                self.driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr[{i}]/td[8]/a').click()
                break
        el_name = self.find_element(self.driver, Locators.input_product_name)
        self.old_name = self.random_name
        self.create_name()
        self.new_name = self.random_name
        el_name.clear()
        el_name.send_keys(self.new_name)
        self.find_element(self.driver, Locators.button_save_products).click()
        self.find_element(self.driver, Locators.tbody_tr_products)

    def remove_product(self):
        self.create_product()
        items = self.find_elements(self.driver, Locators.tbody_tr_products)
        for i in range(1, (len(items) + 1)):
            if self.random_name in self.driver.find_element_by_xpath(
                    f'//*[@id="form-product"]/div/table/tbody/tr[{i}]').get_attribute('textContent'):
                self.driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr[{i}]/td[1]/input').click()
        self.find_element(self.driver, Locators.button_remove_product).click()
        Alert(self.driver).accept()

    def get_url(self):
        return self.driver.get(f'{self.url}index.php?route=product/product&path=57&product_id=49')

    def filter(self):
        self.find_element(self.driver, Locators.input_prod_name_filer).send_keys(self.random_name)
        self.find_element(self.driver, Locators.buttom_filter).click()
        self.find_element(self.driver, Locators.form_product)




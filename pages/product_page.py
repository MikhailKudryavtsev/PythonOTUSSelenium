import allure
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.admin_page import AdminPage


class ProductPage(BasePage):

    button_add_product = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    input_product_name = (By.CSS_SELECTOR, 'input#input-name1')
    input_meta_title = (By.CSS_SELECTOR, 'input#input-meta-title1')
    input_model = (By.CSS_SELECTOR, 'input#input-model')
    button_save_products = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button')
    tbody_tr_products = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr')
    catalog = (By.XPATH, '//*[@id="menu-catalog"]/a')
    products = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    button_remove_product = (By.CSS_SELECTOR, 'button.btn.btn-danger')
    input_prod_name_filer = (By.CSS_SELECTOR, 'input#input-name')
    buttom_filter = (By.CSS_SELECTOR, 'button#button-filter')
    form_product = (By.CSS_SELECTOR, 'form#form-product')
    tbody_tr_td3 = (By.XPATH, '//*[@id="form-product"]/div/table/tbody/tr/td[3]')
    h1_device_name = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
    button_add_card = (By.CSS_SELECTOR, 'button#button-cart')
    container_product = (By.ID, 'product-product')
    nav_tabs = (By.CLASS_NAME, 'nav-tabs')
    data = (By.LINK_TEXT, 'Data')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_product(self):
        self.browser_logs()
        self.proxy_logs()
        self.create_name()
        self.open_products()
        with allure.step("Создание продукта"):
            self.find_element(self.driver, self.button_add_product).click()
            self.logger.info(f'Clicked element: {self.button_add_product}')
            self.find_element(self.driver, self.input_product_name).send_keys(self.random_name)
            self.logger.info(f'Entered text {self.random_name} in "{self.input_product_name}"')
            self.find_element(self.driver, self.input_meta_title).send_keys('TestTagTitle')
            self.logger.info(f'Entered text "TestTagTitle" in {self.input_meta_title}')
            self.find_element(self.driver, self.data).click()
            self.logger.info(f'Clicked element: {self.data}')
            self.find_element(self.driver, self.input_model).send_keys('TestModel')
            self.logger.info(f'Entered text "TestModel" in {self.input_model}')
            self.find_element(self.driver, self.button_save_products).click()
            self.logger.info(f'Clicked element: {self.button_save_products}')
            self.find_element(self.driver, self.tbody_tr_products)


    def open_products(self):
        self.browser_logs()
        self.proxy_logs()
        admin_page = AdminPage(self.driver)
        admin_page.get_url()
        admin_page.authorization_admin()
        with allure.step("Открытие вкладки каталог"):
            self.find_element(self.driver, self.catalog).click()
            self.logger.info(f'Clicked element: {self.catalog}')
        with allure.step("Открытие вкладки продукты"):
            self.find_element(self.driver, self.products).click()
            self.logger.info(f'Clicked element: {self.products}')

    def product_change(self):
        with allure.step("Изменение продукта"):
            self.browser_logs()
            self.proxy_logs()
            self.create_product()
            items = self.find_elements(self.driver, self.tbody_tr_products)
            for i in range(1, (len(items) + 1)):
                if self.random_name in self.driver.find_element_by_xpath(
                        f'//*[@id="form-product"]/div/table/tbody/tr[{i}]').get_attribute('textContent'):
                    self.driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr[{i}]/td[8]/a').click()
                    break
            el_name = self.find_element(self.driver, self.input_product_name)
            self.old_name = self.random_name
            self.create_name()
            self.new_name = self.random_name
            el_name.clear()
            self.logger.info(f'Cleared element: {el_name}')
            el_name.send_keys(self.new_name)
            self.logger.info(f'Entered text "{self.new_name}" in {el_name}')
            self.find_element(self.driver, self.button_save_products).click()
            self.logger.info(f'Clicked element: {self.button_save_products}')
            self.find_element(self.driver, self.tbody_tr_products)

    def remove_product(self):
        with allure.step("Удаление продукта"):
            self.browser_logs()
            self.proxy_logs()
            self.create_product()
            items = self.find_elements(self.driver, self.tbody_tr_products)
            for i in range(1, (len(items) + 1)):
                if self.random_name in self.driver.find_element_by_xpath(
                        f'//*[@id="form-product"]/div/table/tbody/tr[{i}]').get_attribute('textContent'):
                    self.driver.find_element_by_xpath(f'//*[@id="form-product"]/div/table/tbody/tr[{i}]/td[1]/input').click()
            self.find_element(self.driver, self.button_remove_product).click()
            self.logger.info(f'Clicked element: {self.button_remove_product}')
            Alert(self.driver).accept()
            self.logger.info(f'Clicked Alert')

    def get_url(self):
        url = f'{self.url}index.php?route=product/product&path=57&product_id=49'
        self.logger.info(f'Opening url: {url}')
        return self.driver.get(url)

    def filter(self):
        self.browser_logs()
        self.proxy_logs()
        with allure.step("Ввод названия продукта"):
            self.find_element(self.driver, self.input_prod_name_filer).send_keys(self.random_name)
        self.logger.info(f'Entered text "{self.random_name}" in {self.input_prod_name_filer}')
        with allure.step("Нажатие на фильтр"):
            self.find_element(self.driver, self.buttom_filter).click()
        self.logger.info(f'Clicked element: {self.buttom_filter}')
        self.find_element(self.driver, self.form_product)

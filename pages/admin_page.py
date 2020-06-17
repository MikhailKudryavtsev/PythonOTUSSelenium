import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):

    input_username = (By.CSS_SELECTOR, 'input#input-username')
    input_password = (By.CSS_SELECTOR, 'input#input-password')
    button_login = (By.CSS_SELECTOR, 'button.btn.btn-primary')
    img_user_profile = (By.CSS_SELECTOR, 'img#user-profile.img-circle')
    buttom_logout = (By.XPATH, '//*[@id="header"]/div/ul/li[2]/a')
    panel_heading = (By.CSS_SELECTOR, 'h1.panel-title')
    footer = (By.ID, 'footer')
    panel_title = (By.CLASS_NAME, 'panel-title')
    form_Forgotten_Password = (By.CSS_SELECTOR, 'div.panel.panel-default')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_admin = f'{self.url}admin/'
        self.username = 'user'
        self.password = 'bitnami1'

    def authorization_admin(self):
        with allure.step("Авторизаия"):
            self.browser_logs()
            self.proxy_logs()
            self.find_element(self.driver, self.input_username).send_keys(self.username)
            self.logger.info(f'Entered "{self.username}" in {self.input_username}')
            self.find_element(self.driver, self.input_password).send_keys(self.password)
            self.logger.info(f'Entered "{self.password}" in {self.input_password}')
            self.find_element(self.driver, self.button_login).click()
            self.logger.info(f'Clicked element: {self.button_login}')
        with allure.step("Поиск элементов"):
            self.find_element(self.driver, self.img_user_profile)

    def logout_admin(self):
        with allure.step("Выход из аккаунта"):
            self.browser_logs()
            self.proxy_logs()
            self.find_element(self.driver, self.buttom_logout).click()
            self.logger.info(f'Clicked element: {self.buttom_logout}')
        with allure.step("Поиск элементов"):
            self.find_element(self.driver, self.panel_heading)

    def get_url(self):
        self.logger.info(f'Opening url: {self.url_admin}')
        return self.driver.get(self.url_admin)

    def open_form_ForgottenPassword(self):
        self.browser_logs()
        self.proxy_logs()
        self.find_element(self.driver, self.link_Forgotten_Password).click()

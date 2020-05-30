from locators import Locators
from pages.base_page import BasePage

class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_admin = f'{self.url}admin/'

    def authorization_admin(self):
        self.find_element(self.driver, Locators.input_username).send_keys('user')
        self.find_element(self.driver, Locators.input_password).send_keys('bitnami1')
        self.find_element(self.driver, Locators.button_login).click()
        self.find_element(self.driver, Locators.img_user_profile)

    def logout_admin(self):
        self.find_element(self.driver, Locators.buttom_logout).click()
        self.find_element(self.driver, Locators.panel_heading)

    def get_url(self):
        return self.driver.get(self.url_admin)

    def open_form_ForgottenPassword(self):
        self.find_element(self.driver, Locators.link_Forgotten_Password).click()


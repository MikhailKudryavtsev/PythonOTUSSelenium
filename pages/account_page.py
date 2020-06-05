from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    list_group = (By.XPATH, '//*[@id="column-right"]/div')
    button_Continue = (By.CSS_SELECTOR, 'a.btn.btn-primary')
    container_account_login = (By.ID, 'account-login')
    navbar_header = (By.CLASS_NAME, 'navbar-header')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_account_login = f'{self.url}index.php?route=account/login'

    def get_url(self):
        return self.driver.get(self.url_account_login)

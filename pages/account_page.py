from pages.base_page import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_account_login = f'{self.url}index.php?route=account/login'

    def get_url(self):
        return self.driver.get(self.url_account_login)

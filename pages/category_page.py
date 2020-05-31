from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):

    navbar = (By.CSS_SELECTOR, 'ul.nav.navbar-nav')
    left_column = (By.ID, 'column-left')
    swiper_viewport = (By.CLASS_NAME, 'swiper-viewport')
    link_Desktops = (By.LINK_TEXT, 'Desktops')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_category = f'{self.url}index.php?route=product/category&path=20'

    def get_url(self):
        return self.driver.get(self.url_category)

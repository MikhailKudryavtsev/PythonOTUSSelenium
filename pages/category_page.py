from pages.base_page import BasePage


class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_category = f'{self.url}index.php?route=product/category&path=20'

    def get_url(self):
        return self.driver.get(self.url_category)

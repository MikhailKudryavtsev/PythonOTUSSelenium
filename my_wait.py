
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyVisibilityOfSelector:

    def __init__(self, driver, locator, selector):
        self.driver = driver
        self.locator = locator
        self.selector = selector

    def wdw(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((self.locator, self.selector)))

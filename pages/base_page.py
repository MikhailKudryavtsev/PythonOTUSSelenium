import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost/'


    def find_element(self, driver, locator):
        return WebDriverWait(driver, 15).until(EC.visibility_of_element_located(locator),
                                               message=f"Can't find element by locator {locator}")

    def find_elements(self, driver, locator):
        return WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located(locator),
                                               message=f"Can't find elements by locator {locator}")

    def create_name(self):
        letters = string.ascii_lowercase
        self.random_name = ''.join(random.choice(letters) for i in range(8))
        return self.random_name

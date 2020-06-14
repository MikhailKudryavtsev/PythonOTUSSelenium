import logging
import random
import string

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    link_OpenCart = (By.LINK_TEXT, 'OpenCart')
    button_search = (By.XPATH, '//*[@id="search"]/span/button')
    link_Forgotten_Password = (By.LINK_TEXT, 'Forgotten Password')


    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://localhost:82/'
        self.logger = logging.getLogger(type(self).__name__)

    def find_element(self, driver, locator):
        return WebDriverWait(driver, 15).until(EC.visibility_of_element_located(locator),
                                               message=f"Can't find element by locator {locator}")


    def find_elements(self, driver, locator):
        return WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located(locator),
                                               message=f"Can't find elements by locator {locator}")

    def create_name(self):
        letters = string.ascii_lowercase
        self.random_name = ''.join(random.choice(letters) for i in range(8))
        self.logger.info(f'Random Name Generated: "{self.random_name}"')
        return self.random_name

    def browser_logs(self):
        browser = self.driver.get_log("browser")
        for item in browser:
            self.logger.info(f'Error from browser console: {item}')
            allure.attach(body=f'Error from browser console: {item}',
                          name="logs browser",
                          attachment_type=allure.attachment_type.TEXT)

    def proxy_logs(self):
        har = self.driver.proxy.har['log']['entries']
        for item in har:
            self.logger.info(f'Proxy log: {item}')

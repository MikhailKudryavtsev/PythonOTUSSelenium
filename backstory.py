import random
import string
from my_wait import MyVisibilityOfSelector
from selenium.webdriver.common.by import By

class CreateProduct:

    def backstory(self, url, driver):
        self.create_name()
        driver.get(f'{url}admin/')
        selector = 'input#input-username'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector).send_keys('user')
        selector = 'input#input-password'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector).send_keys('bitnami1')
        driver.find_element_by_css_selector('button.btn.btn-primary').click()
        selector = '//*[@id="menu-catalog"]/a'
        MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
        driver.find_element_by_xpath(selector).click()
        selector = '//*[@id="collapse1"]/li[2]/a'
        MyVisibilityOfSelector(driver, By.XPATH, selector).wdw()
        driver.find_element_by_xpath(selector).click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a').click()
        selector = 'input#input-name1'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector).send_keys(self.random_name)
        selector = 'input#input-meta-title1'
        driver.find_element_by_css_selector(selector).send_keys('TestTagTitle')
        driver.find_element_by_link_text('Data').click()
        selector = 'input#input-model'
        MyVisibilityOfSelector(driver, By.CSS_SELECTOR, selector).wdw()
        driver.find_element_by_css_selector(selector).send_keys('TestModel')
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()

    def create_name(self):
        letters = string.ascii_lowercase
        self.random_name = ''.join(random.choice(letters) for i in range(8))
        return self.random_name
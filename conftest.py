import pytest

from pages.account_page import AccountPage
from pages.admin_page import AdminPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions

from pages.start_page import StartPage


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        default="chrome",
        help="This is webdriver for start browser"
    )

    parser.addoption(
        "--url",
        default="http://localhost/",
        help="This is URL opencart"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    driver = request.config.getoption("--driver")
    if driver == 'chrome':
        options = ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("-ignore-certificate-errors")
        options.headless = True
        wd = webdriver.Chrome(options=options)
        request.addfinalizer(wd.quit)
        return wd
    elif driver == 'firefox':
        options = FirefoxOptions()
        options.headless = True
        wd = webdriver.Firefox(options=options)
        request.addfinalizer(wd.quit)
        return wd
    elif driver == 'ie':
        wd = webdriver.Ie()
        request.addfinalizer(wd.quit)
        return wd


@pytest.fixture
def product(driver):
    page = ProductPage(driver)
    return page

@pytest.fixture
def admin(driver):
    page = AdminPage(driver)
    page.get_url()
    return page

@pytest.fixture
def category(driver):
    page = CategoryPage(driver)
    page.get_url()
    return page

@pytest.fixture
def account(driver):
    page = AccountPage(driver)
    page.get_url()
    return page

@pytest.fixture
def start_page(url, driver):
    page = StartPage(url, driver)
    page.get_url()
    return page


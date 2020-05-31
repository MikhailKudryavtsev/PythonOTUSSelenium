import pytest
import logging
import urllib.parse
from browsermobproxy import Server, Client
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from pages.account_page import AccountPage
from pages.admin_page import AdminPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.start_page import StartPage

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s : %(message)s', level=logging.INFO,
                    filename="Opencart.log")

class Mylogger(AbstractEventListener):

    def before_quit(self, driver):
        logger.info(f'Getting ready for completion: "{driver}"')

    def after_quit(self, driver):
        logger.info(f'Completed: "{driver}"')

    def on_exception(self, exception, driver):
        logger.error(f'Something went wrong: {exception}')
        original = f"{exception}.png"
        screenshot = original.replace("/", "")
        product.driver.save_screenshot(screenshot)


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
def proxy_server(request):
    server = Server("browsermob-proxy/bin/browsermob-proxy")
    server.start()
    client = Client("localhost:8080")
    server.create_proxy()
    request.addfinalizer(server.stop)
    client.new_har()
    return client


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request, proxy_server):
    driver = request.config.getoption("--driver")
    if driver == 'chrome':
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
        options = ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("-ignore-certificate-errors")
        proxy_url = urllib.parse.urlparse(proxy_server.proxy).path
        options.add_argument('--proxy-server=%s' % proxy_url)
        options.headless = True
        options.add_experimental_option('w3c', False)
        wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=caps, options=options), Mylogger())
        wd.proxy = proxy_server
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

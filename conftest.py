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
        driver.save_screenshot(screenshot)


def pytest_addoption(parser):
    parser.addoption("--driver", default="chrome", help="This is webdriver for start browser")
    parser.addoption("--url", default="http://192.168.0.102:82/", help="This is URL opencart")
    parser.addoption("--browser", action="store", default="opera", choices=["chrome", "firefox", "opera", "yandex"])
    parser.addoption("--executor", action="store", default="localhost")


@pytest.fixture
def proxy_server(request):
    server = Server("browsermob-proxy/bin/browsermob-proxy", options={"port": 8081})
    server.start()
    client = Client("localhost:82")
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
        request.addfinalizer(wd.quit)
        return wd


@pytest.fixture
def product(browser):
    page = ProductPage(browser)
    return page

@pytest.fixture
def admin(browser):
    page = AdminPage(browser)
    page.get_url()
    return page


@pytest.fixture
def category(browser):
    page = CategoryPage(browser)
    page.get_url()
    return page


@pytest.fixture
def account(browser, url):
    page = AccountPage(browser, url)
    page.get_url()
    return page


@pytest.fixture
def start_page(url, browser):
    page = StartPage(url, browser)
    page.get_url()
    return page


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities={"browserName": browser})
    wd.implicitly_wait(15)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def remote2(request):
    desired_cap = {
     'browser': 'IE',
     'browser_version': '8.0',
     'os': 'Windows',
     'os_version': '7',
     'resolution': '1024x768',
     'name': 'Bstack-[Python] Sample Test'
    }
    wd = webdriver.Remote(
        command_executor='http://bsuser70664:HQksrCDXwqH6w7vwFhUA@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    wd.implicitly_wait(15)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    selenoid = request.config.getoption("--executor")
    executor_url = f"http://{selenoid}:4444/wd/hub"
    caps = {"browserName": browser,
            "enableVnc": True,
            "enableVideo": True,
            "enableLog": True,
            "name": request.node.name}
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    driver = EventFiringWebDriver(driver, Mylogger())
    request.addfinalizer(driver.quit)
    return driver
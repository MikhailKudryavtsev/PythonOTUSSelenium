import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


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

import allure
from selenium.common.exceptions import TimeoutException


@allure.feature("Поиск элементов на странницах")
@allure.story("Страница start_page")
@allure.title("Тест элемены на странице start_page")
def test_start_page(start_page):
    try:
        with allure.step("Поиск элементов на странице start_page"):
            start_page.find_element(start_page.driver, start_page.your_store)
            start_page.find_element(start_page.driver, start_page.button_cart)
            start_page.find_element(start_page.driver, start_page.form_currency)
            start_page.find_element(start_page.driver, start_page.list_buttons)
            start_page.find_element(start_page.driver, start_page.link_MacBook)
            print('\nВсе элементы найдены')
    except TimeoutException as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)


@allure.feature("Поиск элементов на странницах")
@allure.story("Страница account-login")
@allure.title("Тест элемены на странице account-login")
def test_login_page(account):
    try:
        with allure.step("Поиск элементов на странице account-login"):
            account.find_element(account.driver, account.list_group)
            account.find_element(account.driver, account.button_Continue)
            account.find_element(account.driver, account.container_account_login)
            account.find_element(account.driver, account.navbar_header)
            account.find_element(account.driver, account.link_Forgotten_Password)
            print('\nВсе элементы найдены')
    except TimeoutException as e:
        allure.attach(body=account.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)


@allure.feature("Поиск элементов на странницах")
@allure.story("Страница category")
@allure.title("Тест элемены на странице category")
def test_category_page(category):
    try:
        with allure.step("Поиск элементов на странице category"):
            category.find_element(category.driver, category.button_search)
            category.find_element(category.driver, category.navbar)
            category.find_element(category.driver, category.left_column)
            category.find_element(category.driver, category.swiper_viewport)
            category.find_element(category.driver, category.link_Desktops)
            print('\nВсе элементы найдены')
    except TimeoutException as e:
        allure.attach(body=category.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)


@allure.feature("Поиск элементов на странницах")
@allure.story("Страница admin")
@allure.title("Тест элемены на странице admin")
def test_admin_login(admin):
    try:
        with allure.step("Поиск элементов на странице admin"):
            admin.find_element(admin.driver, admin.input_username)
            admin.find_element(admin.driver, admin.input_password)
            admin.find_element(admin.driver, admin.footer)
            admin.find_element(admin.driver, admin.panel_title)
            admin.find_element(admin.driver, admin.link_OpenCart)
        print('\nВсе элементы найдены')
    except TimeoutException as e:
        allure.attach(body=admin.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)


@allure.feature("Поиск элементов на странницах")
@allure.story("Страница product")
@allure.title("Тест элемены на странице product")
def test_product_id(product):
    with allure.step("Переход на страницу с product"):
        product.get_url()
    try:
        with allure.step("Поиск элементов на странице product"):
            product.find_element(product.driver, product.h1_device_name)
            product.find_element(product.driver, product.button_add_card)
            product.find_element(product.driver, product.container_product)
            product.find_element(product.driver, product.nav_tabs)
            product.find_element(product.driver, product.link_OpenCart)
            print('\nВсе элементы найдены')
    except TimeoutException as e:
        allure.attach(body=product.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)

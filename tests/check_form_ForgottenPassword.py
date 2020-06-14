import allure
from selenium.common.exceptions import TimeoutException


@allure.title("Тест проверки формы Forgotten Password")
def test_check_form_ForgottenPassword(admin):
    with allure.step("Открытие url"):
        admin.get_url()
    with allure.step("Открытие формы Forgotten Password"):
        admin.open_form_ForgottenPassword()
    try:
        with allure.step("Поиск элемента"):
            admin.find_element(admin.driver, admin.form_Forgotten_Password)
    except TimeoutException as e:
        allure.attach(body=admin.driver.get_screenshot_as_png(),
                      name="screenshot_image",
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)

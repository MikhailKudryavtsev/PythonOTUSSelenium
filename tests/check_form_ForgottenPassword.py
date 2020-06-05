import pytest
from selenium.common.exceptions import TimeoutException


def test_check_form_ForgottenPassword(admin):
    admin.get_url()
    admin.open_form_ForgottenPassword()
    try:
        admin.find_element(admin.driver, admin.form_Forgotten_Password)
    except TimeoutException:
        pytest.fail('\nНе открылась форма "Забыли пароль?"')

import pytest
from selenium.common.exceptions import TimeoutException


def test_login_and_logout_of_admin(admin):
    try:
        admin.authorization_admin()
        print('\nПроизошла авторизация')
        try:
            admin.logout_admin()
            print('\nПроизошел разлогин')
        except TimeoutException:
            pytest.fail(f'\nРазлогин не произошел')
    except TimeoutException:
        pytest.fail(f'\nАвторизация не произошла')

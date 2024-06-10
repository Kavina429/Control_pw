from control_test.control_selenium.test_step import *

@pytest.mark.smoke_market
def test_login_successful(browser, selenium_action, login_valid):
    """Проверка входа с валидными данными"""
    login_valid()

@pytest.mark.smoke_market
def test_logout_failed(browser, selenium_action, login_not_valid):
    """Проверка отказа входа с невалидными данными"""
    login_not_valid()

@pytest.mark.smoke_market
def test_logout_successful(browser, selenium_action, logout):
    """Проверка выхода"""
    logout()
from control_test.control_selenium.config import *
from control_test.control_selenium.locator import *
from control_test.control_selenium.data import *

"""ПРОВЕРКИ"""

@pytest.fixture
def login_valid(browser, selenium_action):
    def login_valid_function():
        browser.get(data_stend)
        selenium_action.action_fill_input(locator_field_username, data_username)
        selenium_action.action_fill_input(locator_field_user_password, data_password)
        selenium_action.action_click_element(locator_button_login)
        assert "https://the-internet.herokuapp.com/secure" in browser.current_url.lower()
        print('\n--- Вход успешный ---')
    yield login_valid_function

@pytest.fixture
def login_not_valid(browser, selenium_action):
    def login_not_valid_function():
        browser.get(data_stend)
        selenium_action.action_fill_input(locator_field_user_password, data_password)
        selenium_action.action_click_element(locator_button_login)
        successful_text = selenium_action.action_get_text(locator_flash)
        assert successful_text == "Your username is invalid!\n×"
        print('\n--- Вход не выполнен ---')
    yield login_not_valid_function


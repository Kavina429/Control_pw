import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.action import SeleniumAction
import os

# Функция для получения пути к драйверу
def get_driver_path(browser_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    webdriver_dir = os.path.join(current_dir, "webdrivers")
    if browser_name.lower() == 'chrome':
        return os.path.join(webdriver_dir, "chromedriver.exe")
    elif browser_name.lower() == 'yandex':
        return os.path.join(webdriver_dir, "yandexdriver.exe")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

# Фикстура для создания браузера
@pytest.fixture(params=['yandex'])
def browser(request):
    browser_name = request.param
    driver_path = get_driver_path(browser_name)
    if browser_name.lower() == 'chrome':
        service = ChromeService(executable_path=driver_path)
        options_c = ChromeOptions()
        options_c.add_argument("-headless")
        options_c.add_argument("user-agent=Firefox")
        driver = webdriver.Chrome(service=service, options=options_c)
    elif browser_name.lower() == 'yandex':
        service = ChromeService(executable_path=driver_path)
        options_y = ChromeOptions()
        options_y.add_experimental_option('w3c', True)
        driver = webdriver.Chrome(service=service, options=options_y)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    # driver.quit()

# Фикстура для создания объекта SeleniumAction
@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action
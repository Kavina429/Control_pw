import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from control_test.control_pw.data import *
from control_test.control_pw.locator import *


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def browser_context(browser):
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()

@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def login_valid(page: Page):
    def login_valid_func():
        page.goto(data_stend)
        page.fill(locator_field_username, data_username)
        page.wait_for_timeout(1000)
        page.fill(locator_field_password, data_password)
        page.wait_for_timeout(1000)
        page.click(locator_button_login)
        page.wait_for_timeout(1000)
        text_content = page.inner_text("#flash")
        assert "You logged into a secure area!" in text_content
        page.screenshot(path="control_pw/screenshots/login_valid.png")
    return login_valid_func

@pytest.fixture
def login_not_valid(page: Page):
    def login_not_valid_func():
        page.goto(data_stend)
        page.fill(locator_field_password, data_password)
        page.wait_for_timeout(1000)
        page.click(locator_button_login)
        page.wait_for_timeout(1000)
        text_content = page.inner_text("#flash")
        assert "Your username is invalid!" in text_content
        page.screenshot(path="control_pw/screenshots/login_not_valid.png")
    return login_not_valid_func
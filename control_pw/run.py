import pytest
from control_test.control_pw.test import *
from playwright.sync_api import Page

@pytest.mark.smoke
def test_login_valid(page: Page, login_valid):
    login_valid()

@pytest.mark.smoke
def test_login_not_valid(page: Page, login_not_valid):
    login_not_valid()
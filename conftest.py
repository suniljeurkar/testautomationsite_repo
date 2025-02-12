import time
from playwright.sync_api import Playwright
import pytest

from FinalRun.APIutils.create_user import create_users
from FinalRun.UIUtils.browserUtils import BrowserInstance
from FinalRun.UIUtils.dataUtils import userCreds_2
import time

import pytest
from playwright.sync_api import Playwright

from FinalRun.APIutils.create_user import create_users
from FinalRun.UIUtils.browserUtils import BrowserInstance
from FinalRun.UIUtils.dataUtils import userCreds_2


@pytest.fixture(scope="session", autouse=True)
def create_users_before_tests(playwright: Playwright):
    #
    print("\n🔹 Creating Users via API before test execution...")

    created_users = []  # List to store created users

    for user in userCreds_2():
        user_data = create_users(playwright, user)  # Call API to create user
        created_users.append(user_data)  # Store created user credentials
    return created_users  # Return created users


@pytest.fixture(scope="function")
def browser(playwright: Playwright):
    """Setup browser"""
    browser_instance = BrowserInstance(playwright)
    yield browser_instance
    print("Closing the browser")  # for debugging , the browser is not closing after first test is complete
    browser_instance.browser.close()


class UtilsConf:
    def __init__(self, browser_instance: BrowserInstance):
        self.page = browser_instance.page

    def get_cart_data(self):
        time.sleep(2)  # issue with webserver , it returns null value if does not load
        cart_label = self.page.locator(".wc-block-mini-cart__button").get_attribute("aria-label")
        if not cart_label:  # If cart_label is None or empty, return 0 # Added cause its returning value error
            return 0
        words = cart_label.split()
        if words[0].isdigit():
            return int(words[0])  # Convert only if it's a number
        return 0

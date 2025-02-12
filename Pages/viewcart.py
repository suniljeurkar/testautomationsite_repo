import time

from FinalRun.UIUtils.browserUtils import BrowserInstance


class ViewCart:
    def __init__(self, browser_instance: BrowserInstance):
        self.user_details = None
        self.page = browser_instance.page

    def view_cart(self):
        # Navigates to checkout and enters shipping details
        time.sleep(2)  # reduced to 2
        self.page.locator(".wc-block-mini-cart__badge").click()
        self.page.get_by_text("View my cart").click()
        self.page.get_by_text("Proceed to Checkout").click()

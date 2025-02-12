import time

from FinalRun.UIUtils.browserUtils import BrowserInstance


class Checkout:

    def __init__(self, browser_instance: BrowserInstance):
        self.page = browser_instance.page

    def proceed_to_checkout(self, checkout_details):
        # Fill shipping details
        # validating if old orders were placed / all personal details were filled previously
        edit_button = self.page.locator(".wc-block-components-address-card__edit")
        if edit_button.get_attribute("aria-expanded") == "false":  # failing for visiblity , now checking with attribute
            print("Shipping details are already filled. Proceeding to place order...")
        else:
            print("Shipping details are empty. Filling the form...")
            self.page.locator("#shipping-first_name").fill(checkout_details["sFirstName"])
            self.page.locator("#shipping-last_name").fill(checkout_details["sLastName"])
            self.page.locator("#shipping-address_1").fill(checkout_details["sAdd1"])
            self.page.locator("#shipping-city").fill(checkout_details["sCity"])
            self.page.locator("#shipping-postcode").fill(checkout_details["sPostCode"])
            time.sleep(4)  # give time for pincode validation #update  no need now
        self.page.wait_for_selector("button:has-text('Place order')", timeout=60000).click()
        # self.page.locator("button:has-text('Place order')").click() #blocked for testing

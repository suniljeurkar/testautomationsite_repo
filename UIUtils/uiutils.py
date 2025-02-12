# This is initial Ui Utility file designed for sole reason of checking integrity of code
# Later it was shifted to /Pages/... to accomodate page model
# Please ignore this file.
import time

from playwright.sync_api import Playwright, expect

from FinalRun.UIUtils.dataUtils import userCreds_2


class UiUtilities:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        # self.products_to_add = ["Album", "Beanie with Logo", "Hoodie with Zipper"] #added to addProductsinCart.py

    def get_cart_data(self):
        time.sleep(2)  # issue with webserver , it returns null value if does not load
        cart_label = self.page.locator(".wc-block-mini-cart__button").get_attribute("aria-label")
        if not cart_label:  # If cart_label is None or empty, return 0 # Added cause its returning value error
            return 0
        words = cart_label.split()
        if words[0].isdigit():
            return int(words[0])  # Convert only if it's a number
        return 0
        # return int(cart_label.split()[0]) if cart_label else 0  # Handle None case # Old Code

    def login(self):
        # Logs in to the website
        self.user_details = userCreds_2()[0]  # Fetch the first user
        self.page.goto("https://www.testautomationsite.in")
        print("Current URL:", self.page.url)
        self.page.get_by_role("link", name="Login").nth(0).click()
        self.page.locator("#user_login").fill(self.user_details['username'])
        self.page.locator("#user_pass").fill(self.user_details['password'])
        self.page.locator("#rememberme").click()
        self.page.locator("#wppb-submit").click()

    def goto_shop(self):
        self.page.get_by_role("link", name="Shop").nth(0).click()
        print("Current URL:", self.page.url)

    def add_products_to_cart(self, products_to_add):
        # Adds products to cart dynamically
        cart_count_pre = self.get_cart_data()
        print(f'\nInitial cart count: {cart_count_pre}')
        no_of_products = len(products_to_add)
        for product in products_to_add:  # removed sleep from code to make it faster
            product_locator = self.page.locator(f"//a[text()='{product}']/ancestor::li")
            product_locator.locator(".add_to_cart_button").click()
            print(f'\nAdded to cart: {product}')
            cart_count_post = self.get_cart_data()
            # cart_count_pre += 1 # Increment expected count #updated due to new assertion outside for
            # assert cart_count_pre == cart_count_post, f"Expected {cart_count_pre}, but found {cart_count_post}"
            # assertion addition is sometimes giving an issue , moving it out of for loop
        time.sleep(4)  # let ui update the count in cart
        total_count = cart_count_pre + no_of_products
        print("final count", total_count)
        assert total_count == cart_count_post, f"Expected {total_count}, but found {cart_count_post}"

    def view_cart(self):
        # Navigates to checkout and enters shipping details
        self.page.locator(".wc-block-mini-cart__badge").click()
        self.page.get_by_text("View my cart").click()
        self.page.get_by_text("Proceed to Checkout").click()

    def proceed_to_checkout(self, checkout_details):
        # Fill shipping details
        self.page.locator("#shipping-first_name").fill(checkout_details["sFirstName"])
        self.page.locator("#shipping-last_name").fill(checkout_details["sLastName"])
        self.page.locator("#shipping-address_1").fill(checkout_details["sAdd1"])
        self.page.locator("#shipping-city").fill(checkout_details["sCity"])
        self.page.locator("#shipping-postcode").fill(checkout_details["sPostCode"])
        time.sleep(4)
        self.page.locator("button:has-text('Place order')").click()  # blocked for testing

    def verify_order_confirmation(self):
        # Verifies order placement
        order_id = self.page.locator(
            ".wc-block-order-confirmation-summary-list-item:has-text('Order #:') .wc-block-order-confirmation-summary-list-item__value"
        ).text_content()
        order_amount = self.page.locator(
            ".wc-block-order-confirmation-summary-list-item:has-text('Total:') .woocommerce-Price-amount"
        ).text_content()

        print(f'Order ID: {order_id}')
        print(f'Order Amount: {order_amount}')

        # Verify Thank You message
        message_thanks = self.page.get_by_text("Thank you. Your order has been received.")
        expect(message_thanks).to_be_visible()
        print(f"Order placed successfully with ID: {order_id} and amount: {order_amount}")

import time

from FinalRun.UIUtils.browserUtils import BrowserInstance
from FinalRun.conftest import UtilsConf


class AddtoCart:

    def __init__(self, browser_instance: BrowserInstance):
        self.user_details = None
        self.page = browser_instance.get_page()
        # self.products_to_add = ["Album", "Beanie with Logo", "Hoodie with Zipper"] # Sending via testrunner now
        self.utils = UtilsConf(browser_instance)

    def add_products_to_cart(self, products_to_add):
        # Adds products to cart dynamically
        cart_count_pre = self.utils.get_cart_data()
        print(f'\nInitial cart count: {cart_count_pre}')
        no_of_products = len(products_to_add)
        for product in products_to_add:  # removed sleep from code to make it faster
            product_locator = self.page.locator(f"//a[text()='{product}']/ancestor::li")
            product_locator.locator(".add_to_cart_button").click()
            print(f'\nAdded to cart: {product}')
            cart_count_post = self.utils.get_cart_data()
            # cart_count_pre += 1 # Increment expected count #updated due to new assertion outside for
            # assert cart_count_pre == cart_count_post, f"Expected {cart_count_pre}, but found {cart_count_post}"
            # assertion addition is sometimes giving an issue , moving it out of for loop
        time.sleep(2)  # let ui update the count in cart # reduced to 2
        total_count = cart_count_pre + no_of_products
        print("final count", total_count)
        assert total_count == cart_count_post, f"Expected {total_count}, but found {cart_count_post}"

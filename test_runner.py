import time

import pytest
from finalCode_testautomationsite.Pages.PlaceOrder import PlaceOrder
from finalCode_testautomationsite.Pages.addProductsinShop import AddtoCart
from finalCode_testautomationsite.Pages.checkout import Checkout
from finalCode_testautomationsite.Pages.gotoShop import ShopPage
from finalCode_testautomationsite.Pages.login import LoginPage
from finalCode_testautomationsite.Pages.viewcart import ViewCart
from finalCode_testautomationsite.UIUtils.dataUtils import userCreds_2


@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize("user", userCreds_2())  # added new parameterization to code
class TestRunner:
    def test_testrunner(self, browser, user):  # Use the fixture as a parameter, user as parameter

        print(f"Starting Test Execution for the user {user['username']}")
        if not browser:
            pytest.fail("Browser instance is None. It might have been closed prematurely.")

        # Step 1: Login
        print("Logging in...")
        login = LoginPage(browser)
        login.test_login(user)  # passing the new user credentials value

        # Step 2: Navigate to Shop
        time.sleep(2)  # give some sleep for the UI to load properly , cause slow webserver
        print("Navigating to Shop...")
        shop = ShopPage(browser)
        shop.goto_shop()

        # Step 3: Add Products to Cart
        print("Adding Products to Cart...")
        add_to_cart = AddtoCart(browser)
        add_to_cart.add_products_to_cart(["Album", "Beanie with Logo", "Hoodie with Zipper"])

        # Step 4: View Cart
        print("Viewing Cart...")
        view_cart = ViewCart(browser)
        view_cart.view_cart()
        checkout_details = {
            "sFirstName": "John",
            "sLastName": "Doe",
            "sAdd1": "123 Test Street",
            "sCity": "TestCity",
            "sPostCode": "123456"
        }

        # Step 5: Proceed to Checkout
        print("Proceeding to Checkout...")
        checkout = Checkout(browser)
        checkout.proceed_to_checkout(checkout_details)

        # Step 6: Place Order
        print("Placing Order...")
        place_order = PlaceOrder(browser)
        place_order.verify_order_confirmation()

        print(f"Test Execution Completed Successfully for the user {user['username']}")
        browser.close_browser()

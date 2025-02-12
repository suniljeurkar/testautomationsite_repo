import csv
import time
from random import sample

import pytest

from FinalRun.Pages.PlaceOrder import PlaceOrder
from FinalRun.Pages.addProductsinShop import AddtoCart
from FinalRun.Pages.checkout import Checkout
from FinalRun.Pages.gotoShop import ShopPage
from FinalRun.Pages.login import LoginPage
from FinalRun.Pages.viewcart import ViewCart
from FinalRun.UIUtils.dataUtils import userCreds_2


# for running use pytest .\FinalRun\test_runner.py --browser-name=firefox/chromium/edge
# from random import random has some issue , so directly imported sample
# This solved the error


def get_products_from_csv(file_path="C:/Users/sunil/PycharmProjects/TestAutomationSiteE2E/FinalRun/data/products.csv"):
    products = []  # create empty list to take products in
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header  ( We can keep header if needed, but column start with product so removing it )
        for row in reader:
            if row:  # this returns true when it has value , cause python inteprets value as true blank as false
                products.append(row[0])  # Add the product to the list
        return products

@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize("user", userCreds_2())  # added new parameterization to code
class TestRunner:
    @pytest.mark.smoke
    def test_testrunner_smoke(self, browser, user):  # Use the fixture as a parameter, user as parameter

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

    @pytest.mark.regression
    def test_testrunner_regression(self, browser, user):  # Use the fixture as a parameter, user as parameter

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

        # Step 3: Get products from CSV and randomly select products
        available_products = get_products_from_csv()
        selected_products = sample(available_products,
                                   k=3)  # Select 3 random products # will randomize k in next version
        print(f"Selected Products for {user['username']}: {selected_products}")

        # Step 4: Add Products to Cart
        print("Adding Products to Cart...")
        add_to_cart = AddtoCart(browser)
        add_to_cart.add_products_to_cart(selected_products)

        # Step 5: View Cart
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

        # Step 6: Proceed to Checkout
        print("Proceeding to Checkout...")
        checkout = Checkout(browser)
        checkout.proceed_to_checkout(checkout_details)

        # Step 7: Place Order
        print("Placing Order...")
        place_order = PlaceOrder(browser)
        place_order.verify_order_confirmation()

        print(f"Test Execution Completed Successfully for the user {user['username']}")
        browser.close_browser()

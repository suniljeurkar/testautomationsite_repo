
from playwright.sync_api import expect

from FinalRun.UIUtils.browserUtils import BrowserInstance


class PlaceOrder():
    def __init__(self, browser_instance: BrowserInstance):
        self.page = browser_instance.page

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

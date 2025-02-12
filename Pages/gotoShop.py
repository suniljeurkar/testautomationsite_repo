from FinalRun.UIUtils.browserUtils import BrowserInstance


class ShopPage:

    def __init__(self, browser_instance: BrowserInstance):
        self.page = browser_instance.get_page()

    def goto_shop(self):
        self.page.get_by_role("link", name="Shop").nth(0).click()
        print("Current URL:", self.page.url)

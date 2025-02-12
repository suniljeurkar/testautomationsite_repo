from playwright.sync_api import Playwright


class BrowserInstance:
    #
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        self.page.goto("https://testautomationsite.in/")

    def get_page(self):
        return self.page

    def close_browser(self):
        ##print ("Closing the browser")
        self.browser.close()  # see if it helps

from playwright.sync_api import Playwright


class BrowserInstance:
    #
    def __init__(self, playwright: Playwright, browser_select: str):  # set browser_select as string
        if browser_select == "chromium":
            self.browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        elif browser_select == "firefox":
            self.browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])
        elif browser_select == "webkit":
            self.browser = playwright.webkit.launch(headless=False, args=["--start-maximized"])
        else:
            raise ValueError(f'Unspported browser : {browser_select}')
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        self.page.goto("https://testautomationsite.in/")

    def get_page(self):
        return self.page

    def close_browser(self):
        ##print ("Closing the browser")
        self.browser.close()  # see if it helps

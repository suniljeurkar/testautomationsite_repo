from finalCode_testautomationsite.conftest import userCreds_2, BrowserInstance


class LoginPage:
    def __init__(self, browser_instance: BrowserInstance):
        # self.user_details = None  # no need of this now
        self.page = browser_instance.page

    def test_login(self, user):
        # Logs in to the website
        # Accpeting new userdata from json file
        self.user_details = userCreds_2()[0]  # Fetch the first user
        # print("Current URL:", self.page.url) # for debugging , now code runs fine
        print(f"Logging in with: {user['username']}")
        self.page.get_by_role("link", name="Login").nth(
            0).click()  # nth(0) multiple same link , from DOM we can access first
        self.page.locator("#user_login").fill(user['username'])  # logging using parameters recieved.
        self.page.locator("#user_pass").fill(user['password'])
        self.page.locator("#rememberme").click()
        self.page.locator("#wppb-submit").click()

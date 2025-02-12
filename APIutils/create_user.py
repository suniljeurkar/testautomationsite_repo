import pytest
import pytest_check as check
from playwright.sync_api import Playwright

from FinalRun.UIUtils.dataUtils import userCreds_2


@pytest.mark.parametrize('userCreds', userCreds_2())
def create_users(playwright: Playwright, userCreds):
    setUsername = userCreds["username"]
    setPassword = userCreds["password"]
    setEmail = userCreds["email"]
    # userCreds = {'setUsername':'testuser012', 'setEmail': 'testuser012@testautomationsite.in', 'setPassword' :'Pass123@' }
    api_req_context = playwright.request.new_context(base_url="https://www.testautomationsite.in")
    response_send = api_req_context.post(
        url="/wp-json/custom/v1/register",
        data={
            "username": setUsername,
            "email": setEmail,
            "password": setPassword
        },
        headers={"Content-Type": "application/json"}
    )
    # Print response for debugging if needed
    print("User Creation response ", response_send.json())
    print('\n Status Code:', response_send.status)
    print('\n Status:', response_send.status_text)

    # Assert
    # assert response_send.status == 200, f"Expected 200 but got {response_send.status}"
    # hard asserts causing issue while the user is already generated ,
    # moving to soft assert
    check.equal(response_send.status, 200, f"Expected 200 but got {response_send.status}")
    if response_send.status == 400 and "user_exists" in response_send.json().get("code", ""):
        print(f"User {setUsername} already exists. Skipping creation.")
    else:
        check.equal(response_send.status, 200, f"Expected 200 but got {response_send.status}")
        # for other errors excluding duplicate user

    creds_send = {"username": setUsername, "password": setPassword}
    print("credentials created", creds_send)  # for debugging
    return creds_send  # Ensure function returns created user credentials

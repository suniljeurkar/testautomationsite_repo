# this is for manual run
# may not work after more changes done due to some code issues
# need to revisit if required

import pytest
from finalCode_testautomationsite.APIutils.create_user import create_users
from finalCode_testautomationsite.conftest import userCreds_2
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def test_create_api(playwright: Playwright):
    user_list = userCreds_2()
    created_user_list = []  # blank canvas to enter value

    for user_data in user_list:
        login_details = create_users(playwright, user_data)
        created_user_list.append(login_details)  # appending each iteration into list
        print("login username", login_details['username'])  # print each time user is created for debugging
        print("login password", login_details['password'])  # print each time user is created for debugging

    print(login_details)  # print final list
    return created_user_list  # returning list of created user for parameterization

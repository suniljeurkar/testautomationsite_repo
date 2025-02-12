import json


def userCreds_2():
    #
    with open("C:/Users/sunil/PycharmProjects/TestAutomationSiteE2E/FinalRun/data/usercredentials.json") as f:
        testValue = json.load(f)
    return testValue["userCredentials"]

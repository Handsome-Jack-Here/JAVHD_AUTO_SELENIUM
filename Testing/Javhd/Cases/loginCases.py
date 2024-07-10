from Javhd.Locators.locators import LOCATORS
from TestingValues.values import POSITIVE
from URLS.urls import urls
from caseAndSuiteMethods import DICTIONARY

LOGIN_PAGE_LOCATORS = LOCATORS.login_page_locators

LOG_IN_POSITIVE_CASE = [
    {
        DICTIONARY.locator: LOGIN_PAGE_LOCATORS.button_login_page,
        DICTIONARY.steps: {
            DICTIONARY.click: True,
            DICTIONARY.compare_url: urls.login_page,
        }
    },
    {
        DICTIONARY.locator: LOGIN_PAGE_LOCATORS.user_name,
        DICTIONARY.steps: {
            DICTIONARY.input: POSITIVE.users.paid_user.username,
        }
    },
    {
        DICTIONARY.locator: LOGIN_PAGE_LOCATORS.password,
        DICTIONARY.steps: {
            DICTIONARY.input: POSITIVE.users.paid_user.password,
        }
    },
    {
        DICTIONARY.locator: LOGIN_PAGE_LOCATORS.login_button,
        DICTIONARY.steps: {
            DICTIONARY.click: True,
            DICTIONARY.compare_url: urls.main_page,
        }
    },
]

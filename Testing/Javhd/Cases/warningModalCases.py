from Javhd.Locators.locators import LOCATORS
from caseAndSuiteMethods import DICTIONARY

WARNING_MODAL_LOCATORS = LOCATORS.warning_modal
ALERT = LOCATORS.alert

WARNING_AGREE_CASE = [
    {
        DICTIONARY.locator: WARNING_MODAL_LOCATORS.button_agree,
        DICTIONARY.steps: {
            DICTIONARY.click: True,
        }
    },
]

ALERT_CANCEL_CASE = [
    {
        DICTIONARY.locator: ALERT.button_cancel,
        DICTIONARY.steps: {
            DICTIONARY.click: True,
        },
    },
]

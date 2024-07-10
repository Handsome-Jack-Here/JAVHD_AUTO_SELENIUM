from Javhd.Locators.locators import LOCATORS
from caseAndSuiteMethods import DICTIONARY

MAIN_PAGE_LOCATORS = LOCATORS.main_page

CHECK_TOP_CATEGORY_POSITIVE_CASE = [
    {
        DICTIONARY.locator: MAIN_PAGE_LOCATORS.top_category_block,
        DICTIONARY.steps: {
            DICTIONARY.click: True,
        }
    },
    {
        DICTIONARY.locator: MAIN_PAGE_LOCATORS.some_category,
        DICTIONARY.steps: {
            DICTIONARY.click: True,
        }
    },
]

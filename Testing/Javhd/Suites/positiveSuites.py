from Cases import loginCases, warningModalCases, mainPageCases
from Javhd.URLS.urls import urls
from caseAndSuiteMethods import DICTIONARY
LOG_IN_POSITIVE_SUITE = {
    DICTIONARY.url: urls.main_page,
    DICTIONARY.test_cases: [
        *warningModalCases.ALERT_CANCEL_CASE,
        *warningModalCases.WARNING_AGREE_CASE,
        *loginCases.LOG_IN_POSITIVE_CASE,
        *mainPageCases.CHECK_TOP_CATEGORY_POSITIVE_CASE,
    ]
}



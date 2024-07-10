from dotmap import DotMap

LOCATORS = DotMap(
    {
        'login_page_locators': {
            'button_login_page': '//*[@id="app"]/header/div/div/div/div/div/div[2]/div[2]/a',
            'user_name': '//*[@id="login"]',
            'password': '//*[@id="password"]',
            'login_button': '//*[@id="loginform"]/div[4]/input',
        },
        'warning_modal': {
            'button_agree': '//*[@id="warningPopup"]/div/button',
            'button_disagree': '//*[@id="warningPopup"]/div/div[2]/a',
        },
        'alert': {
            'button_cancel': '//*[@id="onesignal-slidedown-cancel-button"]',
            'button_allow': '//*[@id="onesignal-slidedown-allow-button"]'
        },
        'main_page': {
            'top_category_block': '//*[@id="app"]/main/div/div[10]',
            'top_category_preview': '//*[@id="app"]/main/div/div[10]/div/section/div/div',
            'some_category': '//*[@id="app"]/main/div/div[10]/div/section/div/header/div/div/div[1]/div[2]/button',
        },
    }
)

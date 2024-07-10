import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from caseAndSuiteMethods import DICTIONARY


class AutoTestEngine:

    def __init__(self, data: dict, engine: str = 'chrome'):
        self.engine = engine
        self.data = data
        self.steps = None
        self.current_element_locator = None
        self.current_element = None
        self.input_value = None
        self.current_url = None

        self.pause_time = 1
        self.options = webdriver.ChromeOptions()
        # self.options.page_load_strategy = 'normal'  # default await page completely load
        self.options.page_load_strategy = 'eager'  # await only DOM
        # self.options.add_argument('--window-size=1366,1080')
        self.options.add_argument('--incognito')  # incognito
        # self.options.add_argument('--headless')
        self.options.add_argument("--start-maximized")
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=0.2)
        self.action = ActionChains(self.driver)

    def get_page(self, url):
        response = requests.get(url)
        http_code = response.status_code
        assert http_code == 200, f'Page not loaded. Code: {http_code}'
        self.driver.get(url)

    def check_element_available(self, locator):
        element = ('xpath', locator)
        assert self.wait.until(ec.element_to_be_clickable(element)), 'Not found element by locator.'
        self.current_element = self.driver.find_element(*element)
        self.scroll_to_element()

    def scroll_to_element(self):
        self.action.move_to_element(self.current_element).perform()

    def click_on_element(self):
        self.check_element_available(self.current_element_locator)
        self.current_element.click()
        self.await_action()

    def double_click_on_element(self):
        self.check_element_available(self.current_element_locator)
        self.action.double_click(self.current_element).perform()

    def enter_event(self):
        self.current_element.send_keys(Keys.ENTER)

    def tab_event(self):
        self.current_element.send_keys(Keys.TAB)

    def send_keys_to_element(self, value):
        self.current_element.send_keys(value)

    def await_action(self):
        self.action.pause(self.pause_time).perform()

    def compare_url(self, url):
        self.wait.until(ec.url_to_be(self.driver.current_url))
        self.current_url = self.driver.current_url
        assert url in self.current_url, f'Wrong URL'

    def run(self):
        self.driver.delete_all_cookies()
        url = self.data[DICTIONARY.url]
        test_cases = self.data[DICTIONARY.test_cases]
        self.get_page(url)

        for test_case in test_cases:
            self.current_element_locator = test_case[DICTIONARY.locator]
            self.steps = test_case[DICTIONARY.steps]

            self.check_element_available(test_case[DICTIONARY.locator])

            for step in self.steps:

                if step == DICTIONARY.click:
                    if self.steps[step]:
                        self.click_on_element()

                elif step == DICTIONARY.dblclick:
                    if self.steps[step]:
                        self.double_click_on_element()

                elif step == DICTIONARY.input:
                    if self.steps[step]:
                        self.input_value = self.steps[step]
                        self.check_element_available(self.current_element_locator)
                        self.send_keys_to_element(self.input_value)

                elif step == DICTIONARY.enter_event:
                    if self.steps[step]:
                        self.enter_event()

                elif step == DICTIONARY.tab_event:
                    if self.steps[step]:
                        self.tab_event()

                elif step == DICTIONARY.wait:
                    if self.steps[step]:
                        self.await_action()

                elif step == DICTIONARY.compare_url:
                    url = self.steps[step]
                    if url:
                        url = self.steps[step]
                        self.compare_url(url)

        time.sleep(2)
        self.driver.close()
        print(f'All OK')

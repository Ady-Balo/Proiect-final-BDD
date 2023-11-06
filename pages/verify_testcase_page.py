from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class TestCasePage(HomePage, BasePage):
    URL="https://automationexercise.com/"
    TEST_CASE_BUTTON=(By.CSS_SELECTOR, "a[href='/test_cases']")
    TEST_CASE_PAGE=(By.CSS_SELECTOR, "#scrollUp")

    def navigate_to_home(self):
        self.browser.get(self.URL)

    def click_on_testcase_button(self):
        self.find(self.TEST_CASE_BUTTON)
        self.click(self.TEST_CASE_BUTTON)

    def navigate_to_testcase_page(self):
        self.is_displayed(self.TEST_CASE_PAGE)

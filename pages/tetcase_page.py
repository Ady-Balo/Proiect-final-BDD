from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class TestCasePage(HomePage):
    URL="https://automationexercise.com/"
    TEST_CASE_BUTTON=(By.CSS_SELECTOR, "a[href='/test_cases']")
    TEST_CASE_PAGE=(By.CSS_SELECTOR, "#scrollUp")

    def navigate_to_home(self):
        self.browser.get(self.URL)

    def click_on_testcase_button(self):
        self.browser.find_element(*self.TEST_CASE_BUTTON).click()

    def navigate_to_testcase_page(self):
        self.browser.find_element(*self.TEST_CASE_PAGE)
        # time.sleep(2)

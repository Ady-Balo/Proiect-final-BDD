from selenium.webdriver.common.by import By

from browser import Browser


class HomePage(Browser):
    URL="https://automationexercise.com/"
    HOME_LOC=(By.LINK_TEXT, "Home")
    SIGNUP_LOC=(By.PARTIAL_LINK_TEXT, "Signup")

    def navigate_to_home(self):
        self.browser.get(self.URL)

    def verify_home_page(self):
        return self.browser.find_element(*self.HOME_LOC).text

    def click_on_signup(self):
        self.browser.find_element(*self.SIGNUP_LOC).click()

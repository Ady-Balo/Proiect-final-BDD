from selenium.webdriver.common.by import By

from pages.home_page import HomePage


# login whit incorrect email and pass

class InvalidLoginPage(HomePage):
    URL="https://automationexercise.com/"
    SIGNUP_LOC=(By.PARTIAL_LINK_TEXT, "Signup")
    LOG_EMAIL=(By.XPATH, "//input[@data-qa='login-email']")
    LOG_PASS=(By.XPATH, "//input[@data-qa='login-password']")
    LOG_ACC_MSG=(By.XPATH, "//div[@class = 'login-form']/h2")
    LOG_BUTTON=(By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MSG=(By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")

    def click_on_login_button(self):
        self.browser.find_element(*self.SIGNUP_LOC).click()

    def login_to_your_account_message(self):
        return self.browser.find_element(*self.LOG_ACC_MSG).is_displayed()

    def enter_invalid_username(self):
        self.browser.find_element(*self.LOG_EMAIL).send_keys("nemo@email.com")

    def enter_invalid_password(self):
        self.browser.find_element(*self.LOG_PASS).send_keys("nemo1234")

    def click_on_login(self):
        self.browser.find_element(*self.LOG_BUTTON).click()

    def error_message(self):
        self.browser.find_element(*self.ERROR_MSG).is_displayed()

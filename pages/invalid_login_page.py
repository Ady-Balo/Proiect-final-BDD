from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


# login whit incorrect email and pass

class InvalidLoginPage(HomePage, BasePage):
    URL="https://automationexercise.com/"
    SIGNUP_LOC=(By.PARTIAL_LINK_TEXT, "Signup")
    LOG_EMAIL=(By.XPATH, "//input[@data-qa='login-email']")
    LOG_PASS=(By.XPATH, "//input[@data-qa='login-password']")
    LOG_ACC_MSG=(By.XPATH, "//div[@class = 'login-form']/h2")
    LOG_BUTTON=(By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MSG=(By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")

    def click_on_login_button(self):
        self.click(self.SIGNUP_LOC)

    def login_to_your_account_message(self):
        return self.get_text(self.LOG_ACC_MSG)

    def enter_invalid_username(self):
        self.fill_text(self.LOG_EMAIL, "nemo@email.com")

    def enter_invalid_password(self):
        self.fill_text(self.LOG_PASS, "nemo1234")

    def click_on_login(self):
        self.click(self.LOG_BUTTON)

    def error_message(self):
        self.get_text(self.ERROR_MSG)
        return self.find(self.ERROR_MSG).text

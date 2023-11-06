from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL="https://automationexercise.com/login"
    SIGNUP_LOC=(By.PARTIAL_LINK_TEXT, "Signup")
    LOG_ACC_MSG=(By.XPATH, "//div[@class = 'login-form']/h2")
    NEW_USER_LOC=(By.TAG_NAME, "h2")
    USER_LOC=(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_LOC=(By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON_LOC=(By.XPATH, "//button[@data-qa='signup-button']")
    PASSWORD_LOGIN_LOC=(By.XPATH, "//input[@placeholder='Password']")
    EMAIL_LOGIN_LOC=(By.XPATH, "//input[@data-qa='login-email']")
    LOG_USER=(By.LINK_TEXT, "Logged in as test")
    LOGOUT_LOC=(By.CSS_SELECTOR, "a[href='/logout']")
    LOGIN_BUTTON=(By.CSS_SELECTOR, "button[data-qa='login-button']")

    def get_new_user_signup(self):
        return self.browser.find_elements(*self.NEW_USER_LOC)

    def navigate_to_login(self):
        self.browser.get(self.URL)

    def introduce_username(self, username):
        self.fill_text(self.USER_LOC, username)

    def introduce_email(self, email):
        self.fill_text(self.EMAIL_LOC, email)

    def click_on_signup(self):
        self.click(self.SIGNUP_BUTTON_LOC)

    def enter_email(self):
        self.fill_text(self.EMAIL_LOGIN_LOC, 'molina@email.com')

    def enter_password(self):
        self.fill_text(self.PASSWORD_LOGIN_LOC, 'lola12')

    def click_on_login(self):
        self.click(self.LOGIN_BUTTON)

    def verify_username(self):
        return self.browser.find_element(*self.LOG_USER).text

    def click_on_logout(self):
        self.click(self.LOGOUT_LOC)

    def verify_login_page(self):
        self.browser.execute_script("scrollTo(0, document.body.scrollHeight);")

from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class LoginPage(HomePage):
    URL="https://automationexercise.com/login"
    SIGNUP_LOC=(By.PARTIAL_LINK_TEXT, "Signup")
    LOG_ACC_MSG=(By.XPATH, "//div[@class = 'login-form']/h2")
    NEW_USER_LOC=(By.TAG_NAME, "h2")
    USER_LOC=(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_LOC=(By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON_LOC=(By.XPATH, "//button[@data-qa='signup-button']")

    def get_new_user_signup(self):
        return self.browser.find_elements(*self.NEW_USER_LOC)

    def navigate_to_login(self):
        self.browser.get(self.URL)

    def introduce_username(self):
        self.browser.find_element(*self.USER_LOC).send_keys("testelek1")
        # dupa prima rulare cu comanda <behave> din terminal trebuie schimbata <email>-ul in caz de fail
        # daca nu schimbam o sa avem eroarea "Email already exist!" si nu putem continua registrarea ca "New user!"

    def introduce_email(self):
        self.browser.find_element(*self.EMAIL_LOC).send_keys("testelek1@email.com")

    def click_on_signup(self):
        self.browser.find_element(*self.SIGNUP_BUTTON_LOC).click()

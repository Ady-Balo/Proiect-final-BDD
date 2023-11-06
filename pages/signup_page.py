from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class SignUpPage(HomePage, BasePage):
    URL="https://automationexercise.com/signup"
    ENTER_ACCOUNT=(By.CSS_SELECTOR, "login-form > .text-center.title > b")
    TITLE_LOC=(By.CSS_SELECTOR, "#id_gender1")
    PASS_LOC=(By.ID, "password")
    DAY_LOC=(By.XPATH, '//*[@id="days"]/option[10]')
    MONTH_LOC=(By.XPATH, "//*[@id='months']/option[11]")
    YEAR_LOC=(By.XPATH, "//*[@id='years']/option[3]")
    NEWSLETTER_LOC=(By.XPATH, "//input[@id='newsletter']")
    RECEIVE_LOC=(By.CSS_SELECTOR, "#optin")
    FIRST_NAME_LOC=(By.XPATH, "//input[@id='first_name']")
    LAST_NAME_LOC=(By.CSS_SELECTOR, "#last_name")
    ADDRESS_LOC=(By.CSS_SELECTOR, "#address1")
    COUNTRY_LOC=(By.XPATH, '//*[@id="country"]/option[2]')
    STATE_LOC=(By.XPATH, "//input[@id='state']")
    CITY_LOC=(By.CSS_SELECTOR, "#city")
    ZIPCODE_LOC=(By.CSS_SELECTOR, "#zipcode")
    MOBILE_LOC=(By.CSS_SELECTOR, "#mobile_number")
    CR_ACCOUNT_LOC=(By.CSS_SELECTOR, "button[data-qa='create-account']")
    VR_ACCOUNT=(By.CSS_SELECTOR, "h2[class='title text-center'] b")
    CONTINUE_LOC=(By.LINK_TEXT, "Continue")
    DELETE_ACCOUNT=(By.LINK_TEXT, "Delete Account")
    LOGGED_IN_USER=(By.XPATH, "//li[10]//a[1]")

    def return_enter_account(self):
        return self.browser.find_elements(*self.ENTER_ACCOUNT)

    def fill_title(self):
        self.click(self.TITLE_LOC)

    def fill_password(self):
        self.fill_text(self.PASS_LOC, "test1234")

    def fill_data_birth(self):
        self.click(self.DAY_LOC)
        self.click(self.MONTH_LOC)
        self.click(self.YEAR_LOC)

    def selecting_checkbox1(self):
        self.browser.find_element(*self.NEWSLETTER_LOC).click()

    def selecting_checkbox2(self):
        self.browser.find_element(*self.RECEIVE_LOC).click()

    def introduce_first_name(self):
        self.fill_text(self.FIRST_NAME_LOC, "User")

    def introduce_last_name(self):
        self.fill_text(self.LAST_NAME_LOC, "Tester")

    def introduce_address(self):
        self.fill_text(self.ADDRESS_LOC, "123 Street,Nr.2")

    def introduce_country(self):
        self.browser.find_element(*self.COUNTRY_LOC)

    def introduce_state(self):
        self.fill_text(self.STATE_LOC, "New York")

    def introduce_city(self):
        self.fill_text(self.CITY_LOC, "New York City")

    def introduce_zipcode(self):
        self.fill_text(self.ZIPCODE_LOC, "10001")

    def introduce_mobile_number(self):
        self.fill_text(self.MOBILE_LOC, "1234567890")

    def click_on_create_account(self):
        self.browser.find_element(*self.CR_ACCOUNT_LOC).submit()

    def verify_account_created(self):
        self.browser.find_element(*self.VR_ACCOUNT).is_displayed()

    def click_on_continue_button(self):
        self.click(self.CONTINUE_LOC)

    def verify_logged_in_username(self):
        self.browser.find_element(*self.LOGGED_IN_USER).is_displayed()

    def click_on_delete_account(self):
        self.click(self.DELETE_ACCOUNT)

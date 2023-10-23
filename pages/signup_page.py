from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class SignUpPage(HomePage):
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
        self.browser.find_element(*self.TITLE_LOC).click()

    def fill_password(self):
        self.browser.find_element(*self.PASS_LOC).send_keys("test1234")

    def fill_data_birth(self):
        self.browser.find_element(*self.DAY_LOC).click()
        self.browser.find_element(*self.MONTH_LOC).click()
        self.browser.find_element(*self.YEAR_LOC).click()

    def selecting_checkbox1(self):
        self.browser.find_element(*self.NEWSLETTER_LOC).click()

    def selecting_checkbox2(self):
        self.browser.find_element(*self.RECEIVE_LOC).click()

    def introduce_first_name(self):
        self.browser.find_element(*self.FIRST_NAME_LOC).send_keys("User")

    def introduce_last_name(self):
        self.browser.find_element(*self.LAST_NAME_LOC).send_keys("Tester")

    def introduce_address(self):
        self.browser.find_element(*self.ADDRESS_LOC).send_keys("123 Street,Nr.2")

    def introduce_country(self):
        self.browser.find_element(*self.COUNTRY_LOC)

    def introduce_state(self):
        self.browser.find_element(*self.STATE_LOC).send_keys("New York")

    def introduce_city(self):
        self.browser.find_element(*self.CITY_LOC).send_keys("New York City")

    def introduce_zipcode(self):
        self.browser.find_element(*self.ZIPCODE_LOC).send_keys("10001")

    def introduce_mobile_number(self):
        self.browser.find_element(*self.MOBILE_LOC).send_keys("1234567890")

    def click_on_create_account(self):
        self.browser.find_element(*self.CR_ACCOUNT_LOC).submit()

    def verify_account_created(self):
        self.browser.find_element(*self.VR_ACCOUNT).is_displayed()

    def click_on_continue_button(self):
        self.browser.find_element(*self.CONTINUE_LOC).click()

    def verify_logged_in_username(self):
        self.browser.find_element(*self.LOGGED_IN_USER).is_displayed()

    def click_on_delete_account(self):
        self.browser.find_element(*self.DELETE_ACCOUNT).click()

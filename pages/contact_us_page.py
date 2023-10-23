from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class ContactUsPage(HomePage):
    CONTACT_US_BTN=(By.XPATH, "//a[normalize-space()='Contact us']")
    GET_IN_TOUCH=(By.XPATH, "//h2[normalize-space()='Get In Touch']")
    NAME_INP=(By.NAME, 'name')
    EMAIL_INP=(By.NAME, 'email')
    SUBJECT_INP=(By.NAME, 'subject')
    MESSAGE_INP=(By.NAME, 'message')
    SUBMIT_BTN=(By.XPATH, "//input[@name='submit']")
    HOME_BUTTON=(By.CSS_SELECTOR, ".fa-angle-double-left")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "a[class='btn btn-success'] span")

    def click_on_contact_us_btn(self):
        self.browser.find_element(*self.CONTACT_US_BTN).click()

    def verify_get_in_touch(self):
        self.browser.find_element(*self.GET_IN_TOUCH).is_displayed()

    def fill_name_email_subject_message(self):
        self.browser.find_element(*self.NAME_INP).send_keys('John Doe')
        self.browser.find_element(*self.EMAIL_INP).send_keys('johndoe@example.com')
        self.browser.find_element(*self.SUBJECT_INP).send_keys('Test Subject')
        self.browser.find_element(*self.MESSAGE_INP).send_keys('Test Message')
        # time.sleep(3)

    def click_on_submit_btn(self):
        self.browser.find_element(*self.SUBMIT_BTN).click()

    def click_on_alert_btn(self):
        self.browser.switch_to.alert.accept()
        # time.sleep(3)

    def verify_succes_message(self):
        self.browser.find_element(*self.SUCCESS_MESSAGE)
        # time.sleep(3)

    def click_on_home_btn(self):
        self.browser.find_element(*self.HOME_BUTTON).click()

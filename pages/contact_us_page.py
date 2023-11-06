from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class ContactUsPage(HomePage, BasePage):
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
        self.click(self.CONTACT_US_BTN)

    def verify_get_in_touch(self):
        self.browser.find_element(*self.GET_IN_TOUCH).is_displayed()

    def fill_name_email_subject_message(self):
        self.fill_text(self.NAME_INP, 'John Doe')
        self.fill_text(self.EMAIL_INP, 'johndoe@example.com')
        self.fill_text(self.SUBJECT_INP, 'Test Subject')
        self.fill_text(self.MESSAGE_INP, 'Test Message')

    def click_on_submit_btn(self):
        self.click(self.SUBMIT_BTN)

    def click_on_alert_btn(self):
        self.browser.switch_to.alert.accept()

    def verify_success_message(self):
        self.browser.find_element(*self.SUCCESS_MESSAGE)

    def click_on_home_btn(self):
        self.click(self.HOME_BUTTON)

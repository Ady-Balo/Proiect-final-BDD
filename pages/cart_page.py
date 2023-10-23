from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class CartPage(HomePage):
    URL="https://automationexercise.com/view_cart"
    CART_LOC=(By.CSS_SELECTOR, "a[href='/view_cart']")
    FOOTER_LOC=(By.CSS_SELECTOR, "#footer")
    SUBSCR_TEXT=(By.CSS_SELECTOR, "div[class='single-widget'] h2")
    SUBSCR_EMAIL=(By.XPATH, "//input[@id='susbscribe_email']")
    SUBSCR_ARROW=(By.CSS_SELECTOR, "#subscribe")
    SUCCESS_MSG=(By.CSS_SELECTOR, "#success-subscribe")
    QUANTITY_LOC=(By.CSS_SELECTOR, ".disabled")

    def click_on_cart_button(self):
        self.browser.find_element(*self.CART_LOC)

    def navigate_to_footer(self):
        self.browser.find_element(*self.FOOTER_LOC)

    def verify_text_subscription(self):
        self.browser.find_element(*self.SUBSCR_TEXT).is_displayed()

    def enter_email_and_click_on_arrow_button(self):
        self.browser.find_element(*self.SUBSCR_EMAIL).send_keys("mernl@email.com")
        self.browser.find_element(*self.SUBSCR_ARROW).submit()

    def verify_successfully_message(self):
        self.browser.find_element(*self.SUCCESS_MSG).is_displayed()

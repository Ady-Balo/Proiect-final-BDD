from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    URL="https://automationexercise.com/"
    HOME_LOC=(By.LINK_TEXT, "Home")
    SIGNUP_LOC=(By.PARTIAL_LINK_TEXT, "Signup")
    PRODUCTS_BTN=(By.CSS_SELECTOR, "a[href='/products']")
    ARROW_LOC=(By.XPATH, "//i[@class='fa fa-angle-up']")
    TEXT_VISIBLE=(By.CSS_SELECTOR, "div[class='item active'] div[class='col-sm-6'] h2")
    SUBSCRIPTION_TEXT=(By.CSS_SELECTOR, "div[class='single-widget'] h2")

    def navigate_to_home(self):
        self.browser.get(self.URL)

    def verify_home_page(self):
        return self.get_text(self.HOME_LOC)

    def click_on_signup(self):
        self.click(self.SIGNUP_LOC)

    def verify_home_page_text(self):
        return self.browser.get_text(self.URL)

    def click_on_products_button(self):
        self.click(self.PRODUCTS_BTN)

    def scroll_down_page(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def verify_text_subscription(self):
        return self.get_text(self.SUBSCRIPTION_TEXT)

    def click_on_arrow(self):
        self.click(self.ARROW_LOC)

    def verify_text_visibility(self):
        return self.get_text(self.TEXT_VISIBLE)

    def scroll_up_page(self):
        self.browser.execute_script("window.scrollTo(0,0)")

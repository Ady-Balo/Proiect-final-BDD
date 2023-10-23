from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class ProductsPage(HomePage):
    CART_URL="https://automationexercise.com/view_cart"
    MAN_LOC=(By.XPATH, "//a[normalize-space()='Men']")
    TSHIRT_LOC=(By.XPATH, '//*[@id="Men"]/div/ul/li[1]/a')
    VIEW_TSHIERT_LOC=(By.CSS_SELECTOR, "a[href='/product_details/2']")
    QUANTITY_LOC=(By.CSS_SELECTOR, "#quantity")
    ADD_TO_CART_LOC=(By.XPATH, "//button[@type='button']")
    VIEW_CART_LOC=(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u')
    QUANTITYS_LOC=(By.CSS_SELECTOR, ".disabled")
    QUANTITY_MENU=(By.CSS_SELECTOR, ".quantity")

    def click_on_man_button(self):
        self.browser.find_element(*self.MAN_LOC).click()

    def click_on_tshirt_button(self):
        button=self.browser.find_element(*self.TSHIRT_LOC)
        self.browser.execute_script("arguments[0].click();", button)

    def click_on_view_tshirt_button(self):
        button=self.browser.find_element(*self.VIEW_TSHIERT_LOC)
        self.browser.execute_script("arguments[0].click();", button)

    def enter_quantity(self):
        self.browser.find_element(*self.QUANTITY_LOC).clear()
        self.browser.find_element(*self.QUANTITY_LOC).send_keys("5")

    def click_on_add_to_cart_button(self):
        self.browser.find_element(*self.ADD_TO_CART_LOC).click()

    def click_on_view_cart_button(self):
        button=self.browser.find_element(*self.VIEW_CART_LOC)
        self.browser.execute_script("arguments[0].click();", button)

    def click_on_quantity_button(self):
        button=self.browser.find_element(*self.QUANTITYS_LOC)
        self.browser.execute_script("arguments[0].click();", button)

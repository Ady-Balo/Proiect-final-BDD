from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.home_page import HomePage


class ProductsPage(HomePage, BasePage):
    CART_URL="https://automationexercise.com/view_cart"
    MAN_LOC=(By.XPATH, "//a[normalize-space()='Men']")
    TSHIRT_LOC=(By.XPATH, '//*[@id="Men"]/div/ul/li[1]/a')
    VIEW_TSHIERT_LOC=(By.CSS_SELECTOR, "a[href='/product_details/2']")
    QUANTITY_LOC=(By.CSS_SELECTOR, "#quantity")
    ADD_TO_CART_LOC=(By.XPATH, "//button[@type='button']")
    VIEW_CART_LOC=(By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u')
    QUANTITYS_LOC=(By.CSS_SELECTOR, ".disabled")
    QUANTITY_MENU=(By.CSS_SELECTOR, ".quantity")
    SEARCH_PRODUCT_BOX=(By.XPATH, "//input[@id='search_product']")
    SEARCH_PRODUCT_BTN=(By.XPATH, "//button[@id='submit_search']")
    SEARCHED_PRODUCTS_TXT=(By.XPATH, "//h2[.='Searched Products']")
    SEARCHED_PRODUCTS=(By.XPATH, "//a[@class='btn btn-default add-to-cart']")

    def click_on_man_button(self):
        wait=WebDriverWait(self.browser, 10)
        element=self.browser.find_element(*self.MAN_LOC)
        wait.until(EC.element_to_be_clickable(element))

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
        self.delete_text(self.QUANTITYS_LOC)
        self.fill_text(self.QUANTITYS_LOC, "2")
        self.click(self.QUANTITY_MENU)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_up(self):
        self.browser.execute_script("window.scrollTo(0, 0)")

    def enter_product_name(self):
        self.wait_for_visible_element(self.SEARCH_PRODUCT_BOX, 10)
        self.find(self.SEARCH_PRODUCT_BOX).send_keys('T-Shirt')

    def click_on_search_button(self):
        button=self.browser.find_element(*self.SEARCH_PRODUCT_BTN)
        self.browser.execute_script("arguments[0].click();", button)

    def verify_searched_products(self):
        return self.browser.find_element(*self.SEARCHED_PRODUCTS_TXT).text

    def verify_all_searched_products(self):
        return self.browser.find_elements(*self.SEARCHED_PRODUCTS)

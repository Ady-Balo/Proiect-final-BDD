from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser


class BasePage(Browser):
    def __init__(self):
        super().__init__()

    def open_url(self, url: str):
        self.browser.get(url)

    def get_current_url(self):
        return self.browser.current_url

    def find(self, locator: tuple):
        return self.browser.find_element(*locator)

    def wait_for_visible_element(self, locator: tuple, time: int = 10):
        wait=WebDriverWait(self.browser, time)
        wait.until(expected_conditions.visibility_of_element_located(locator), "Element not visible")

    def get_text(self, locator: tuple, time: int = 10):
        self.wait_for_visible_element(locator, time)
        return self.find(locator).text

    def fill_text(self, locator: tuple, text: str, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).send_keys(text)

    def delete_text(self, locator: tuple, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).clear()

    def click(self, locator: tuple, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).click()

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

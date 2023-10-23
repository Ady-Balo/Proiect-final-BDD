from selenium import webdriver


class Browser:
    browser=webdriver.Firefox()
    browser.fullscreen_window()
    browser.implicitly_wait(5)

    def close(self):
        self.browser.quit()





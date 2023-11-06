from selenium import webdriver


class Browser:
    browser=webdriver.Firefox()
    browser.fullscreen_window()
    browser.implicitly_wait(5)

    def close_popup(self, popup):
        self.browser.implicitly_wait(5)
        if self.browser.switch_to.default_content() is None:
            self.browser.switch_to.frame(popup)
            self.browser.switch_to.default_content()





    def close(self):
        self.browser.quit()





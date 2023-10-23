from browser import Browser
from pages.cart_page import CartPage
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.invalid_login_page import InvalidLoginPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.signup_page import SignUpPage
from pages.tetcase_page import TestCasePage


def before_all(context):
    """
    Se executa la inceperea tuturor testelor
    """

    context.browser=Browser()
    context.home_page=HomePage()
    # context.base_page = Basepage()
    context.login_page=LoginPage()
    context.signup_page=SignUpPage()
    context.invalid_login_page=InvalidLoginPage()
    context.cart_page=CartPage()
    context.testcase_page=TestCasePage()
    context.contact_us_page=ContactUsPage()
    context.products_page=ProductsPage()


def after_all(context):
    """
        Se executa la terminarea tuturor testelor
    """
    context.browser.close()

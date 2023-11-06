from behave import *


# login whit incorrect email and pass


@when("Click on ' Login ' button")
def step_impl(context):
    context.home_page.click_on_login_button()


@when("Verify 'Login to your account' is visible")
def step_impl(context):
    context.invalid_login_page.login_to_your_account_message()


@step("Enter invalid email address and password")
def step_impl(context):
    context.invalid_login_page.enter_invalid_username()
    context.invalid_login_page.enter_invalid_password()


@when("Click 'login' button")
def step_impl(context):
    context.invalid_login_page.click_on_login()


@then("Verify that 'Your email or password is incorrect!' is visible")
def step_impl(context):
    context.invalid_login_page.error_message()

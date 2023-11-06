from behave import *


# all the step_impl methods for the signup feature -> signup_page

@given("I am on the signup page")
def step_impl(context):
    context.signup_page.return_enter_account()


@when("I fill the title, password and data birth")
def step_impl(context):
    context.signup_page.fill_title()
    context.signup_page.fill_password()
    context.signup_page.fill_data_birth()


@step("Selecting  checkbox 'Sign up for our newsletter!'")
def step_impl(context):
    context.signup_page.selecting_checkbox1()


@step("Selecting checkbox 'Receive special offers from our partners!'")
def step_impl(context):
    context.signup_page.selecting_checkbox2()


@when("I fill first name, last name, address, country,state, city, zipcode, mobile Number")
def step_impl(context):
    context.signup_page.introduce_first_name()
    context.signup_page.introduce_last_name()
    context.signup_page.introduce_address()
    context.signup_page.introduce_country()
    context.signup_page.introduce_state()
    context.signup_page.introduce_city()
    context.signup_page.introduce_zipcode()
    context.signup_page.introduce_mobile_number()


@step("I click 'Create Account button'")
def step_impl(context):
    context.signup_page.click_on_create_account()


@then("I verify that 'ACCOUNT CREATED!' is visible")
def step_impl(context):
    context.signup_page.verify_account_created()


@step("I click 'Continue' button")
def step_impl(context):
    context.signup_page.click_on_continue_button()


@then("I verify 'Logged in as username' is visible")
def step_impl(context):
    context.signup_page.verify_logged_in_username()


@then("I click the 'Delete Account' button")
def step_impl(context):
    context.signup_page.click_on_delete_account()

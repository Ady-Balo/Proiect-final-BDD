from behave import *


# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test

# new user signup

@when("Click on 'Signup / Login ' button")
def step_impl(context):
    context.home_page.click_on_signup()


@then("'New User Signup!' is visible")
def step_impl(context):
    lista_h2=context.login_page.get_new_user_signup()
    new_user=False
    for element in lista_h2:
        if element.text == "New User Signup!":
            new_user=True
    assert new_user


@given("I am on the login page")
def step_impl(context):
    context.login_page.navigate_to_login()


@when("I enter a valid {username} and a valid {email}")
def step_impl(context, username, email):
    context.login_page.introduce_username(username)
    context.login_page.introduce_email(email)


@step("I click Signup")
def step_impl(context):
    context.login_page.click_on_signup()


@then("'ENTER ACCOUNT INFORMATION' is visible")
def step_impl(context):
    account_info=context.signup_page.return_enter_account()
    expected_text='ENTER ACCOUNT INFORMATION'

    for element in account_info:
        if element.text == expected_text and element.is_displayed():
            print("'ENTER ACCOUNT INFORMATION' is visible")


@when('I enter correct email address')
def step_impl(context):
    context.login_page.enter_email()


@step('I enter correct password')
def step_impl(context):
    context.login_page.enter_password()


@when("I click 'login' button")
def step_impl(context):
    context.login_page.click_on_login()


@step("Verify that Logged in as username is visible")
def step_impl(context):
    context.login_page.verify_username()


@when("Click Logout button")
def step_impl(context):
    context.login_page.click_on_logout()


@then("Verify that user is navigated to login page")
def step_impl(context):
    context.login_page.verify_login_page()
    return context

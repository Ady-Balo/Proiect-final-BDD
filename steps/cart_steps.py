from behave import *


@when("I click the 'Cart' button")
def step_impl(context):
    context.cart_page.click_on_cart_button()


@step("I scroll down to footer")
def step_impl(context):
    context.cart_page.navigate_to_footer()


@when("I verify text 'SUBSCRIPTION'")
def step_impl(context):
    context.cart_page.verify_text_subscription()


@step("I enter email address in input and click arrow button")
def step_impl(context):
    context.cart_page.enter_email_and_click_on_arrow_button()


@then("I should see message 'You have been successfully subscribed!'")
def step_impl(context):
    context.cart_page.verify_successfully_message()

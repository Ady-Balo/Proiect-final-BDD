from behave import *


@when('I click the Man  button')
def step_impl(context):
    context.products_page.click_on_man_button()


@when('I click the Tshirt  button')
def step_impl(context):
    context.products_page.click_on_tshirt_button()


@step("I select TShirt view product button")
def step_impl(context):
    context.products_page.click_on_view_tshirt_button()


@when("I enter quantity and click Add to Cart button")
def step_impl(context):
    context.products_page.enter_quantity()
    context.products_page.click_on_add_to_cart_button()


@when("I click View cart alert")
def step_impl(context):
    context.products_page.click_on_view_cart_button()


@then("I find the quantity button and click to modify")
def step_impl(context):
    context.products_page.click_on_quantity_button()

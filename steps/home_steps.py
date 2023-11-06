from behave import *


@given("I am on the home page")
def step_impl(context):
    context.home_page.navigate_to_home()


@then("I see a Home option in the menu")
def step_impl(context):
    menu_name=context.home_page.verify_home_page()
    expected_menu_name="Home"
    assert menu_name == expected_menu_name


@step("I verify that home page is visible successfully")
def step_impl(context):
    context.home_page.verify_home_page()
    return context


@step("I click on 'Products' button")
def step_impl(context):
    context.home_page.click_on_products_button()


@step("Scroll down page to bottom")
def step_impl(context):
    context.home_page.scroll_down_page()


@step("Verify text SUBSCRIPTION")
def step_impl(context):
    context.home_page.verify_text_subscription()


@step("Click on arrow at bottom right side to move upward")
def step_impl(context):
    context.home_page.click_on_arrow()


@then("Verify that page is scrolled up to top and Full-Fledged practice website is visible")
def step_impl(context):
    context.home_page.verify_text_visibility()


@step("Scroll up page to top")
def step_impl(context):
    context.home_page.scroll_up_page()

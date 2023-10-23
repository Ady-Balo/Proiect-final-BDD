from behave import *


@given("I am on the home page")
def step_impl(context):
    context.home_page.navigate_to_home()


@then("I see a Home option in the menu")
def step_impl(context):
    menu_name=context.home_page.verify_home_page()
    expected_menu_name="Home"
    assert menu_name == expected_menu_name



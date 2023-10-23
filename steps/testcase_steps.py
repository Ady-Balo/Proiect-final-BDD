from behave import *


# @given("I am on the home page")
# def step_impl(context):
#     context.home_page.navigate_to_home()

@when("I see a Test Case  button in the menu and I click on")
def step_impl(context):
    context.testcase_page.click_on_testcase_button()


@then("Verify that I can  navigate to test cases page successfully")
def step_impl(context):
    context.testcase_page.navigate_to_testcase_page()


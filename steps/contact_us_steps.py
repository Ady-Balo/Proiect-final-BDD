from behave import *


@when("Click on 'Contact Us' button")
def step_impl(context):
    context.contact_us_page.click_on_contact_us_btn()


@step("Verify 'GET IN TOUCH' is visible")
def step_impl(context):
    context.contact_us_page.verify_get_in_touch()


@step("Enter name, email, subject and message")
def step_impl(context):
    context.contact_us_page.fill_name_email_subject_message()


@step("Upload file")
def step_impl(context):
    pass


@then("Click 'Submit' button")
def step_impl(context):
    context.contact_us_page.click_on_submit_btn()


@then("Click on alert button")
def step_impl(context):
    context.contact_us_page.click_on_alert_btn()


@step("Verify success message 'Success! Your details have been submitted successfully.' is visible")
def step_impl(context):
    context.contact_us_page.verify_success_message()


@then("Click 'Home' button and verify that landed to home page successfully")
def step_impl(context):
    context.contact_us_page.click_on_home_btn()

from behave import *
from page_objects.main import LampFrontend
from web_config import BrowserDriver
from variables import locators
from time import sleep

use_step_matcher("re")


@given("That I am on the login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver = LampFrontend()

    # Go to landing page
    context.driver.go_to_home()

    # Click on the login page button
    context.driver.click(locators.login_page_button)
    context.driver.wait_action(locators.login_button)
    # Verify that I am on the login page
    context.driver.verify_action(locators.login_button, 'Login')


@when("I enter my login details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Insert email
    context.driver.insert(locators.email_field, locators.email)

    # Insert password
    context.driver.insert(locators.password_field, locators.password)


@step("I click on the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.login_button)
    context.driver.wait_action(locators.dashbaord_tab)


@then("System should redirect me to the dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.dashbaord_tab, 'Dashboard')


@when("Click on the trainees tab")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.trainees_tab)
    context.driver.wait_action(locators.trainees_page_heading)


@then("System should display trainees page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.trainees_page_heading, locators.trainee_page_header_text)


@step("Display record of existing trainees")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Search for a trainee from record
    context.driver.wait_action(locators.search_field)
    context.driver.insert(locators.search_field, locators.search_email)
    context.driver.verify_action(locators.trainee_record, locators.search_email)


@given("That I am on the trainees page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.trainees_tab)
    context.driver.wait_action(locators.invite_button)


@when("I click on the invite button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.invite_button, 'Invite')
    context.driver.click(locators.invite_button)
    context.driver.wait_action(locators.invite_modal_heading)


@step("I add email to the provided field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sleep(5)
    # Verify that invite modal is shown
    context.driver.verify_action(locators.invite_modal_heading, locators.invite_modal_heading_text)
    # Insert email
    context.driver.insert(locators.invite_email_field, locators.invite_email)
    context.driver.click(locators.invite_add_button)
    # Verify that email is added
    context.driver.verify_action(locators.email_added, locators.invite_email)


@step("I click on the send invite button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sleep(3)
    context.driver.click(locators.send_invite_button)
    context.driver.wait_action(locators.invite_success_modal)


@then("System should display an success page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.invite_success_modal, locators.invite_success_message)
    # Close invite modal
    context.driver.click(locators.invite_close_button)


@step("I have selected a trainee")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verify that I am on the trainees page
    context.driver.verify_action(locators.trainees_page_heading, locators.trainee_page_header_text)

    # Select a trainee
    context.driver.click(locators.trainee_selection_checkbox)


@when("I click on the Assign course action")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Click on the Assign course action
    context.driver.click(locators.assign_course_icon)
    context.driver.wait_action(locators.assign_course_modal)


@step("I select a course")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.assign_course_modal, 'Assign Courses')

    # Click on a course from dropdown
    context.driver.click(locators.assign_course_dropdown)

    # Select course
    context.driver.click(locators.assign_course_select)


@step("click the Assign course button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.assign_course_button)
    sleep(3)


@then("System should display a success message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    messages = ['Course Assigned Successfully', 'Course Already Assigned']
    context.driver.verify_any_message(locators.snackbar_alert, messages)


@given("That I am on the groups page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Got to the trainees tab
    context.driver.click(locators.trainees_tab)
    context.driver.wait_action(locators.groups_tab_button)

    # Click on the groups
    context.driver.click(locators.groups_tab_button)
    context.driver.wait_action(locators.create_group_button)


@when("I click on the create group button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.create_group_button)
    context.driver.wait_action(locators.create_group_modal)


@step("I Select or enter group name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.create_group_modal, 'Create a Group')
    context.driver.click(locators.group_dropdown)

    context.driver.click(locators.select_other_groups)

    # Verify field to enter group name appears
    context.driver.wait_action(locators.group_name_field)

    # Enter group name
    context.driver.insert(locators.group_name_field, '')

@then("System creates group successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then System create group successfully')


@step("Group is added to list of exitsting groups")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Group is added to list of created groups')
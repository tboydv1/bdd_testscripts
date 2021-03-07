from behave import *
from page_objects.main import LampFrontend
from variables import locators
from time import sleep

use_step_matcher("re")


@given("I am logged in as an admin on lamp-frontend")
def step_impl(context):

    context.driver = LampFrontend()
    context.driver.login(locators.email, locators.password)


@when("I click the Trainees tab")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.driver.click(locators.trainees_tab)
    context.driver.wait_action(locators.trainees_page_heading)


@then("I should see the Trainees page and all Trainees")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.trainees_page_heading, locators.trainee_page_header_text)


@when("I search for the for the logged in user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.insert(locators.search_field, locators.search_name)


@then("user should be found")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.search_result, locators.search_result_name)
    sleep(3)


@step("role should be HR")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.search_result, locators.search_result_role)


@when("I click the invite button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.invite_button)
    context.driver.wait_action(locators.invite_modal_heading)


@then("I should see the invite Trainees dialog")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.invite_modal_heading, locators.invite_modal_heading_text)


@when("I insert an email")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.insert(locators.invite_modal_search, locators.invite_email)


@step("I click the Add button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.add_button)


@then("I should be able to add the email successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.email_added, locators.invite_email)


@when("I click the send invite button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.click(locators.send_invite_button)
    context.driver.wait_action(locators.invite_success_modal, locators.invite_success_message)


@then("System displays an invite send modal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_action(locators.invite_success_modal, locators.invite_success_message)


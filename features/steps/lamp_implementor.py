from behave import *
from page_objects.main import LampFrontend
from variables import locators

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

    context.driver.click_trainees_tab()


@then("I should see the Trainees page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.verify_page(locators.trainees_page_heading, locators.trainee_page_header_text)
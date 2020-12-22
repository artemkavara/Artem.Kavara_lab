from behave import *
from page import Base_Page
from locator import Search_Locators

@given("I am on EPAM website")
def step_impl(context):
    context.browser.get('https://www.epam.com/');

@when('I press "Search" buttom')
def step_impl(context):
    page = Base_Page(context)
    page.click_button(Search_Locators.SEARCH_BUTTON)

@then("I should see a text field")
def step_impl(context):
    page = Base_Page(context)
    page.is_search_text_field()

@then('I should see a buttom "Find"')
def step_impl(context):
    page = Base_Page(context)
    page.is_find_button()

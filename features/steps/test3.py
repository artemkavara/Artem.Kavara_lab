from behave import *
from Base_Page import Base_Page_Locators, Base_Page

@given("I am on EPAM website")
def step_impl(context):
    context.page = Base_Page('https://www.epam.com/')

@when('I press "Search" buttom')
def step_impl(context):
    context.page.click_button(Base_Page_Locators.SEARCH_BUTTON)

@then("I should see a text field")
def step_impl(context):
    context.page.is_search_text_field()

@then('I should see a buttom "Find"')
def step_impl(context):
    context.page.is_find_button()
    context.page.browser.quit()

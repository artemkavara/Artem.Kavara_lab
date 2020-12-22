from behave import *
from page import Careers_Page
from locator import Careers_Locators

@given('I am on page "Work with us"')
def step_impl(context):
    context.browser.get("https://www.epam.com/careers")

@when('I press on checkbox "Remote"')
def step_impl(context):
    careers_page =  Careers_Page(context)
    careers_page.click_button(Careers_Locators.REMOTE_BOX)

@when('push the "FIND" buttom')
def step_impl(context):
    careers_page =  Careers_Page(context)
    careers_page.click_button(Careers_Locators.FIND_BUTTON)

@then('I should see the list of only remote job offers')
def step_impl(context):
    careers_page =  Careers_Page(context)
    careers_page.is_correct("REMOTE")

@when('I press on "All Skills" box')
def step_impl(context):
    careers_page =  Careers_Page(context)
    careers_page.click_button(Careers_Locators.ALL_SKILLS)

@then('I should see the list of skills')
def step_impl(context):
    careers_page =  Careers_Page(context)
    careers_page.is_list_found()

@when('I enter {word} in "Keyword or job ID"')
def step_impl(context, word):
    careers_page =  Careers_Page(context)
    careers_page.enter_word_in_field(word)

@then('I should see the list of offers related to {word}')
def step_impl(context, word):
    careers_page =  Careers_Page(context)
    careers_page.click_button(Careers_Locators.FIND_BUTTON)
    careers_page.is_correct(word)
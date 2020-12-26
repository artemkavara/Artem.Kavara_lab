from behave import *
from Careers_Page import Careers_Locators, Careers_Page
from selenium.webdriver.common.action_chains import ActionChains

@given('I am on page "Work with us"')
def step_impl(context):
    context.careers_page = Careers_Page("https://www.epam.com/careers")

@when('I press on checkbox "Remote"')
def step_impl(context):
    context.careers_page.click_button(Careers_Locators.REMOTE_BOX)

@when('push the "FIND" buttom')
def step_impl(context):
    context.careers_page.click_button(Careers_Locators.FIND_BUTTON)

@then('I should see the list of only remote job offers')
def step_impl(context):
    context.careers_page.is_correct("REMOTE")
    context.careers_page.browser.quit()

@when('I press on "All Skills" box')
def step_impl(context):
    context.careers_page.click_button(Careers_Locators.ALL_SKILLS)

@then('I should see the list of skills')
def step_impl(context):
    context.careers_page.is_list_found()
    context.careers_page.browser.quit()
    
@when('I enter {word} in "Keyword or job ID"')
def step_impl(context, word):
    context.careers_page.enter_word_in_field(word)

@then('I should see the list of offers related to {word}')
def step_impl(context, word):
    context.careers_page.click_button(Careers_Locators.FIND_BUTTON)
    context.careers_page.is_correct(word)
    context.careers_page.browser.quit()
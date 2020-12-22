from behave import *
from page import Contact_Page
from locator import Contact_Page_Locators

@given('I am on page "Contact Us"')
def step_impl(context):
    context.browser.get('https://www.epam.com/about/who-we-are/contact');

@when('I click on first field of the form')
def step_impl(context):
    contact_page = Contact_Page(context)
    contact_page.click_button(Contact_Page_Locators.LIST_BOX)

@then("I should see the drop-down list of topics")
def step_impl(context):
    contact_page = Contact_Page(context)
    contact_page.is_list_found()

@when('I am trying to push "SUBMIT" button with blank "Email" and "Phone" fields')
def step_impl(context):
    contact_page = Contact_Page(context)
    contact_page.click_button(Contact_Page_Locators.SUBMIT_BUTTON)

@then("the system should return alert")
def step_impl(context):
    contact_page = Contact_Page(context)
    contact_page.submit()

@then("the form should not be sent")
def step_impl(context):
    contact_page = Contact_Page(context)
    contact_page.is_form_sent()

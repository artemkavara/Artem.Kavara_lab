from behave import *
from Brochure_Page import Brochure_Locators, Brochure_Page

@given('I am on page with brochures')
def step_impl(context):
    context.base_page = Brochure_Page("https://www.epam.com/our-work/brochures/epams-services-for-direct-to-learner-solution-providers")
    
@when('I push on a {button}')
def step_impl(context, button):
    context.base_page.click_button(int(button),Brochure_Locators.SOCIAL_BUTTON)

@then('a {site} window should be opended')
def step_impl(context, site):
    context.base_page.is_site_opened(site)
    context.base_page.browser.quit()
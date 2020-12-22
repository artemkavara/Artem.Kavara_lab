from behave import *
from page import Brochure_Page
from locator import Brochure_Locators

@given('I am on page with brochures')
def step_impl(context):
    context.browser.get("https://www.epam.com/our-work/brochures/epams-services-for-direct-to-learner-solution-providers");
    
@when('I push on a {button}')
def step_impl(context, button):
    base_page = Brochure_Page(context)
    base_page.click_button(int(button),Brochure_Locators.SOCIAL_BUTTON)

@then('a {site} window should be opended')
def step_impl(context, site):
    base_page = Brochure_Page(context)
    base_page.is_site_opened(site)
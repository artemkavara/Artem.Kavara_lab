from behave import *
from Open_Source_Page import Open_Source_Page

@given('I pushed the buttom "Open Source" on the title page of "EPAM" website')
def step_impl(context):
    context.open_source_page = Open_Source_Page("https://www.epam.com/open-source")

@when('I press on {num} {project} square')
def step_impl(context, num, project):
    context.open_source_page.open_project(int(num), project)

@then('a {page} should be opened')
def step_impl(context, page):
    context.open_source_page.is_page_opened(page)
    context.open_source_page.browser.quit()
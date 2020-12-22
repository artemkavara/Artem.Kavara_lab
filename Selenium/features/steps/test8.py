from behave import *
from page import Open_Source_Page

@given('I pushed the buttom "Open Source" on the title page of "EPAM" website')
def step_impl(context):
    context.browser.get("https://www.epam.com/open-source")

@when('I press on {num} {project} square')
def step_impl(context, num, project):
    open_source_page = Open_Source_Page(context)
    open_source_page.open_project(int(num), project)

@then('a {page} should be opened')
def step_impl(context, page):
    open_source_page = Open_Source_Page(context)
    open_source_page.is_page_opened(page)
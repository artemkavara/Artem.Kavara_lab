from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locator import Contact_Page_Locators
import regex as re

class Base_Page(object):

    def __init__(self, context):
        self.context = context
        try:
            context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/button").click()
        except NoSuchElementException:
            pass
    
    
    def click_button(self, loc):
        button = self.context.browser.find_element(*loc)
        actions = ActionChains(self.context.browser)
        actions.move_to_element(button).perform()
        button.click()
    
    def is_search_text_field(self):
        assert self.context.browser.find_element_by_id("new_form_search")
    
    def is_find_button(self):
        assert self.context.browser.find_element_by_class_name("header-search__submit")
    
class Contact_Page(Base_Page):

    def is_list_found(self):
        assert self.context.browser.find_element_by_xpath("//ul[@aria-expanded='true']")
    
    def submit(self):
        assert self.context.browser.find_element_by_class_name("validation-tooltip")

    def is_form_sent(self):
        try:
            self.context.browser.find_element(*Contact_Page_Locators.CAPTCHA_FRAME)
        except NoSuchElementException:
            assert True

    
class Open_Source_Page(Base_Page):

    def open_project(self, i, name):
        but = self.context.browser.find_elements_by_class_name("tile-list__item")[i]
        actions = ActionChains(self.context.browser)
        actions.move_to_element(but).perform()
        but.click()
        but = self.context.browser.find_element_by_partial_link_text(name)
        but.click()

    def is_page_opened(self, name):
        tabs = self.context.browser.window_handles
        self.context.browser.switch_to.window(tabs[-1])
        url = self.context.browser.current_url
        assert re.search(name, url) != None
    
class Careers_Page(Base_Page):

    def click_button_remote(self, loc):
        button = self.context.browser.find_elements(*loc)[-1]
        actions = ActionChains(self.context.browser)
        actions.move_to_element(button).perform()
        button.click()

    def is_correct(self, word):
        results = self.context.browser.find_elements_by_css_selector("li.search-result__item")
        for res in results:
            assert re.search(word, res.text, re.IGNORECASE)
    
    def is_list_found(self):
        assert self.context.browser.find_element_by_class_name("multi-select-dropdown")
    
    def enter_word_in_field(self, word):
        field = self.context.browser.find_element_by_class_name("recruiting-search__input.js-autocomplete")
        field.send_keys(word)

class Brochure_Page(Base_Page):
    def __init__(self, context):
        self.context = context
        self.default_handle = context.browser.current_window_handle
        try:
            context.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/button").click()
        except NoSuchElementException:
            pass
    

    def click_button(self, i, loc):
        button = self.context.browser.find_elements(*loc)[i]
        actions = ActionChains(self.context.browser)
        actions.move_to_element(button).perform()
        button.click()
    
    def is_site_opened(self, name):
        tabs = self.context.browser.window_handles
        self.context.browser.switch_to.window(tabs[-1])
        url = self.context.browser.current_url
        self.context.browser.close()
        self.context.browser.switch_to_window(self.default_handle)
        assert re.search(name, url) != None
    

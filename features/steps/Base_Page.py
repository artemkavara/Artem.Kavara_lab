from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import regex as re

class Base_Page_Locators(object):
    SEARCH_BUTTON = (By.XPATH, "//button[@class = 'header-search__button header__icon']")
    COOKIE_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/button")
    TEXT_FIELD = (By.ID, "new_form_search")
    SUBMIT_BUTTON = (By.CLASS_NAME, "header-search__submit")


class Base_Page(object):

    def __init__(self, path):
        self.browser = webdriver.Chrome()
        self.browser.get(path)
        try:
            self.browser.find_element(*Base_Page_Locators.COOKIE_BUTTON).click()
        except NoSuchElementException:
            pass
    
    def click_button(self, loc):
        button = self.browser.find_element(*loc)
        actions = ActionChains(self.browser)
        actions.move_to_element(button).perform()
        button.click()
    
    def is_search_text_field(self):
        assert self.browser.find_element(*Base_Page_Locators.TEXT_FIELD)
    
    def is_find_button(self):
        assert self.browser.find_element(*Base_Page_Locators.SUBMIT_BUTTON)
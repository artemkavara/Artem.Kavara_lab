from Base_Page import Base_Page
from selenium.webdriver.common.by import By
import regex as re

class Careers_Locators(object):
    REMOTE_BOX = (By.XPATH, '//*[@id="main"]/div[1]/div[3]/section/div/div[2]/div/form/fieldset/div/p[3]')
    FIND_BUTTON = (By.CLASS_NAME, 'recruiting-search__submit')
    ALL_SKILLS = (By.CLASS_NAME, 'selected-params')
    RESULT_SELECTOR = (By.CSS_SELECTOR, "li.search-result__item")
    LIST_LOCATOR = (By.CLASS_NAME, "multi-select-dropdown")
    FIELD_LOCATOR = (By.CLASS_NAME, "recruiting-search__input.js-autocomplete")

class Careers_Page(Base_Page):

    def click_button_remote(self):
        button = self.browser.find_elements(*Careers_Locators.REMOTE_BOX)[-1]
        actions = ActionChains(self.browser)
        actions.move_to_element(button).perform()
        button.click()

    def is_correct(self, word):
        results = self.browser.find_elements(*Careers_Locators.RESULT_SELECTOR)
        for res in results:
            assert re.search(word, res.text, re.IGNORECASE)
    
    def is_list_found(self):
        assert self.browser.find_element(*Careers_Locators.LIST_LOCATOR)
    
    def enter_word_in_field(self, word):
        field = self.browser.find_element(*Careers_Locators.FIELD_LOCATOR)
        field.send_keys(word)

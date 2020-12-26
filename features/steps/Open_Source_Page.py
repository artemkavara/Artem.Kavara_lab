from Base_Page import Base_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import regex as re

class Open_Source_Locators():
    TITLE_PROJECT = (By.CLASS_NAME, "tile-list__item")

class Open_Source_Page(Base_Page):

    def open_project(self, i, name):
        but = self.browser.find_elements(*Open_Source_Locators.TITLE_PROJECT)[i]
        actions = ActionChains(self.browser)
        actions.move_to_element(but).perform()
        but.click()
        but = self.browser.find_element_by_partial_link_text(name)
        but.click()

    def is_page_opened(self, name):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[-1])
        url = self.browser.current_url
        assert re.search(name, url) != None
from Base_Page import Base_Page
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

class Brochure_Locators(object):
    SOCIAL_BUTTON = (By.CLASS_NAME, 'floating-menu__link')
    COOKIE_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[2]/button")

class Brochure_Page(Base_Page):
    def __init__(self, path):
        self.browser = webdriver.Chrome(executable_path=r"C:\Users\akava\Downloads\chromedriver_win32\chromedriver.exe")
        self.browser.get(path)
        self.default_handle = self.browser.current_window_handle
        try:
            self.browser.find_element(*Brochure_Locators.COOKIE_BUTTON).click()
        except NoSuchElementException:
            pass

    def click_button(self, i, loc):
        button = self.browser.find_elements(*loc)[i]
        actions = ActionChains(self.browser)
        actions.move_to_element(button).perform()
        button.click()
    
    def is_site_opened(self, name):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[-1])
        url = self.browser.current_url
        self.browser.close()
        self.browser.switch_to_window(self.default_handle)
        assert re.search(name, url) != None
    
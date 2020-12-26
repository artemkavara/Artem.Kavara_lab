from Base_Page import Base_Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Contact_Page_Locators(object):
    LIST_BOX = (By.CLASS_NAME, 'select2-selection__rendered')
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CAPTCHA_FRAME = (By.XPATH, '//iframe[title="recaptcha challenge"]')
    LIST_PATH = (By.XPATH, "//ul[@aria-expanded='true']")
    SUBMIT_PATH = (By.CLASS_NAME, "validation-tooltip")

class Contact_Page(Base_Page):

    def is_list_found(self):
        assert self.browser.find_element(*Contact_Page_Locators.LIST_PATH)
    
    def submit(self):
        assert self.browser.find_element(*Contact_Page_Locators.SUBMIT_PATH)

    def is_form_sent(self):
        try:
            self.browser.find_element(*Contact_Page_Locators.CAPTCHA_FRAME)
        except NoSuchElementException:
            assert True
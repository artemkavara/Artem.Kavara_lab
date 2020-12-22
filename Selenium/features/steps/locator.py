from selenium.webdriver.common.by import By

class Contact_Page_Locators(object):
    LIST_BOX = (By.CLASS_NAME, 'select2-selection__rendered')
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CAPTCHA_FRAME = (By.XPATH, '//iframe[title="recaptcha challenge"]')

class Search_Locators(object):
    SEARCH_BUTTON = (By.XPATH, "//button[@class = 'header-search__button header__icon']")

class Careers_Locators(object):
    REMOTE_BOX = (By.XPATH, '//*[@id="main"]/div[1]/div[3]/section/div/div[2]/div/form/fieldset/div/p[3]')
    FIND_BUTTON = (By.CLASS_NAME, 'recruiting-search__submit')
    ALL_SKILLS = (By.CLASS_NAME, 'selected-params')

class Brochure_Locators(object):
    SOCIAL_BUTTON = (By.CLASS_NAME, 'floating-menu__link')
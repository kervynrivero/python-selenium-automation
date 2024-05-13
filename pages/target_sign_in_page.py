from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
class TargetSignInPage(Page):
    TERMS_LOCATOR = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")


    def open_sign_in_page(self):
        self.open('https://www.target.com/account/')

    def click_terms_link(self):
        self.click(*self.TERMS_LOCATOR)
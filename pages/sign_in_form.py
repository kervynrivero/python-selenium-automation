from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class SignInFormPage(Page):
    SIGN_IN_FORM = (By.CSS_SELECTOR, '#login')

    def verify_sign_in(self):
        self.find_element(*self.SIGN_IN_FORM)
        #context.driver.find_element(*SIGN_IN_FORM)

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
class TermsAndCondsPage(Page):
    def verify_page_opened(self):
        self.verify_partial_url('terms-conditions/')

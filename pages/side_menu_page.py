from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class SideMenuPage(Page):

    SIGN_IN_DROPDOWN = (By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']")
    def click_sign_in_dropdown(self):

        self.wait_until_clickable_click(*self.SIGN_IN_DROPDOWN)
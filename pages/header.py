from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'a.styles__PrimaryHeaderLink-sc-8s5b77-1.styles__StyledLinkNamedIcon-sc-1e1g60c-1')


    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_go_to_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)
        self.save_screenshot('Clicked_cart')
        #self.driver.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
        sleep(6)

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN_BUTTON)
        #self.input_text(*self.SIGN_IN_BUTTON)


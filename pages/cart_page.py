from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class CartPage(Page):
    TOTAL = (By.CSS_SELECTOR, "div.styles__StyledHeading-sc-1ge2jts-1.bmsjWz")
    CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0']")
    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty', *self.CART_MESSAGE)

    def verify_product(self):
        self.find_element(*self.TOTAL)


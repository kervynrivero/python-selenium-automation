from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class ProductSideBar(Page):
    ADD_2_CART_LOCATOR = (By.CSS_SELECTOR,
                        "[aria-label*='Add to cart']")

    GO_2_KART_LOCATOR = (By.CSS_SELECTOR, "a[href='/cart']")

    def add_to_cart_product(self):
        self.wait_until_clickable_click(*self.ADD_2_CART_LOCATOR)

    def view_cart_click(self):
        self.wait_until_clickable_click(*self.GO_2_KART_LOCATOR)


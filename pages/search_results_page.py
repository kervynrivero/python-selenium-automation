from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_LOCATOR = (By.CSS_SELECTOR, "[id*=addToCartButtonOrTextIdFor13397813]")

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'

    def click_add_to_cart_button(self):
        self.wait_until_clickable_click(*self.PRODUCT_LOCATOR)

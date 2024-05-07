from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0']")

@then('Verify the cart empty message')
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(*CART_MESSAGE).text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

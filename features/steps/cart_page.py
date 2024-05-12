from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0']")


@then('Verify the cart empty message')
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()



from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_MESSAGE = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0']")


@then('Verify the cart empty message')
def verify_cart_empty_message(context):

    context.wait.until(EC.text_to_be_present_in_element(CART_MESSAGE,'Your cart is empty'),
            message='MESSAGE DID NOT APPEAR'
    )
    print('Test Passed')
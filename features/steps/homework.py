from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a.styles__PrimaryHeaderLink-sc-8s5b77-1.styles__CartLink-sc-jff2tp-0.eLNniN.iqZQhg").click()
    sleep(10)

@then('Verify the cart empty message')
def verify_cart_empty(context):
    sleep(7)
    # Verification
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0.lfA-Dem').text
    assert 'Your cart is empty' in actual_text, f"ERROR, TEXT Your cart is empty NOT IN {actual_text}"
    print('TEST PASSED')


@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH,
                            "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
    sleep(5)


@when('Click Sign in from dropdown')
def click_sign_in_dropdown(context):
    context.driver.find_element(By.XPATH,
                        "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']").click()
    sleep(5)

@then('Verify Sign in form opened')
def verify_sign_in(context):
    var =context.driver.find_element(By.CSS_SELECTOR,'form')
    if var is None:
        print('TEST NOT PASSED')
    else:
        print('TEST PASSED !!! FORM OPENED')
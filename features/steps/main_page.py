from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_BUTTON =(By.CSS_SELECTOR, 'a.styles__PrimaryHeaderLink-sc-8s5b77-1.styles__StyledLinkNamedIcon-sc-1e1g60c-1')
SIGN_IN_DROPDOWN=(By.XPATH,"//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']")
SIGN_IN_FORM=(By.CSS_SELECTOR,'form')
SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
PRODUCT_LOCATOR = (By.CSS_SELECTOR, "[id*=addToCartButtonOrTextIdFor13397813]")
PRODUCT_LOCATOR2 = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor13397813.styles__StyledBaseButtonInternal-sc-ysboml-0[aria-label*='Add to cart']")
PRODUCT_LOCATOR3 = (By.CSS_SELECTOR,"a[href='/cart']")
TOTAL = (By.CSS_SELECTOR, "div.styles__StyledHeading-sc-1ge2jts-1.bmsjWz")

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign in from dropdown')
def click_sign_in_dropdown(context):
    #context.driver.find_element(*SIGN_IN_DROPDOWN).click()
    #sleep(5)
    context.wait.until(EC.element_to_be_clickable(SIGN_IN_DROPDOWN)).click()


@then('Verify Sign in form opened')
def verify_sign_in(context):
    context.driver.find_element(*SIGN_IN_FORM)

@when('Click on Sign in')
def click_sign_in(context):

    #context.driver.find_element(*SIGN_IN_BUTTON).click()
    context.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()
    #sleep(5)

@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    #Need to keep sleep after clicking I could not use wait#
    #context.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()


    sleep(6)


@when('Click on cart icon')
def click_cart(context):
    #context.driver.find_element(*CART_ICON).click()
    #sleep(6)
    context.wait.until(EC.element_to_be_clickable(CART_ICON)).click()


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount): # expected_amount = '5'
    expected_amount = int(expected_amount)   # '5' (str) => 5 (int)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'

@when('Adding product to cart')
def add_to_cart(context):

    context.wait.until(EC.element_to_be_clickable(PRODUCT_LOCATOR)).click()
    context.wait.until(EC.element_to_be_clickable(PRODUCT_LOCATOR2)).click()
    context.wait.until(EC.element_to_be_clickable(PRODUCT_LOCATOR3)).click()



    #context.driver.find_element(*PRODUCT_LOCATOR).click()
    #sleep(4)
    #context.driver.find_element(*PRODUCT_LOCATOR2).click()
    #sleep(4)
    #context.driver.find_element(*PRODUCT_LOCATOR3).click()
    #sleep(4)

@then('Verify product in our cart in cart page')
def verify_product(context):
    context.driver.find_element(*TOTAL)

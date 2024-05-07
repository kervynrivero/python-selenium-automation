from selenium.webdriver.common.by import By
from behave import given, then
HEADER_BENEFITS = (By.CSS_SELECTOR, "div.styles__CellItemCopy-sc-3f68hg-7.dAbAee")


@given('Open TargetCircle main page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify TargetCircle has {expected_amount} benefits')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    benefits = context.driver.find_elements(*HEADER_BENEFITS)
    assert len(benefits) == expected_amount, f'Expected {expected_amount} benefits but got {len(benefits)}'

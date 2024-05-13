from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('Open sign in page')
def open_sign_in_app(context):
    context.app.target_sign_in_page.open_sign_in_page()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_sign_in_page.get_current_window()

@when('Click on Target terms and conditions link')
def click_terms_link(context):
    context.app.target_sign_in_page.click_terms_link()
@when('Switch to the newly opened window')
def switch_new_window(context):
    context.app.target_sign_in_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_page_opened(context):
    context.app.terms_and_conds_page.verify_page_opened()

@then('User can close new window and switch back to original')
def close_and_switch(context):
    context.app.terms_and_conds_page.close()
    context.app.terms_and_conds_page.switch_window_by_id(context.original_window)

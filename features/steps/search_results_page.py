from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_result_page.verify_search_results(expected_item)

@then('Verify that URL has {partial_url}')
def verify_search_page_url(context, partial_url):
    #context.app.base_page.verify_partial_url(partial_url)
    context.app.search_result_page.verify_partial_url(partial_url)
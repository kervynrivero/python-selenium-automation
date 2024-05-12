from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='styles__StyledVariationSelectorImage'] [class='styles__StyledWrapper-sc-hijc5f-0 ioqcdg'] [class*='styles__StyledBaseButtonInternal] button")
COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='styles__StyledVariationSelectorImage'] [class='styles__StyledListItem-sc-hijc5f-3 kyXjnj'] button")

SELECTED_COLOR = (By.CSS_SELECTOR,
    "[class*='styles__StyledVariationSelectorImage'] [class='styles__StyledHeaderWrapperDiv-sc-tezx2e-1 jWgzho']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    print(len(colors))
    for color in colors:
        print(color)

        #FORCE HOVER TO MAKE IT CLICKABLE
        ActionChains(context.driver).move_to_element(color).click(color).perform()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text

        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
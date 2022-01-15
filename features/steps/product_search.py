from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {query}')
def Open_product_page(context, query):
    context.driver.get(f'https://www.amazon.com/dp/{query}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black-1', 'Dark Blue', 'Red Wine']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'


   # OPTION



@then('Verify user can click shoes colors')
def Verify_user_click_dif_colors(context):
    expected_colors = ['Beige Pu', 'Black Micro', 'Blush Pu', 'Camel Pu', 'Charcoal Pu', 'Tan Pu']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    actual_colors = []
    for color in colors[:6]:
       color.click()
       actual_colors += [context.driver.find_element(*SELECTED_COLOR).text]
       print(actual_colors)
    assert actual_colors == expected_colors, f'Expected {expected_colors} but got {actual_colors}'



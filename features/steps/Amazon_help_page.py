from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

#PRIVACY = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")
TITLE = (By.CSS_SELECTOR, "a.cs-help-title")


@given('Open Amazon T&C page')
def open_amazon_TC_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088/')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.driver.window_handles)
    print('original_window:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()

@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def verfy_privacy_notice_page_opened(context):
    actual_title = context.driver.find_element(*TITLE).text
    expect_title = 'Help & Customer Service'
    assert actual_title == expect_title, f'the expected{expect_title}, but got {actual_title}'


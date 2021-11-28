from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()

# User can search for solutions of cancelling an order on amazon.

# Open the url
#driver.get('https://www.amazon.com/')

#driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']").click()

# Why is it that when the browser moves to a new tab the codes are not executed?
# driver.find_element(By.XPATH, "//a[@href='/help']").click()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

elem = driver.find_element(By.XPATH, "//input[@type='search']")

elem.send_keys('cancel orders')
driver.find_element(By.XPATH, "//a[@class='same_window cs-override-recommended']").click()

actual_result = driver.find_element(By.XPATH, "//*[contains(text(), 'Cancel Items and Orders')]").text

expected_result = 'Cancel Items and Orders'

assert actual_result == expected_result, f'Error,actual {actual_result} did not match our expected {expected_result}'

print('Test case pass')
driver.quit()


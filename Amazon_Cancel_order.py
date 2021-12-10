from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()

# User can search for solutions of cancelling an order on amazon.

# Open the url

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//input[@type='search']")
search.send_keys('cancel orders')
search.send_keys(Keys.ENTER)

# OR driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order', Keys.ENTER)
#actual_result = driver.find_element(By.XPATH, "//*[contains(text(), 'Cancel Items or Orders')]").text

actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_result = 'Cancel Items or Orders'

assert actual_result == expected_result, f'Expected {expected_result}, but we got {actual_result}'

print('Test case pass')
driver.quit()


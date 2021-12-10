from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()


# Open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_result = '"table"'
assert actual_result == expected_result, f'Error,actual {actual_result} did not match our expected {expected_result}'

print('Test case passed')
driver.quit()
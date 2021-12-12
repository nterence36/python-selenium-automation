from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()


# Open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('zin')

driver.find_element(By.ID, 'nav-search-submit-button').click()
driver.find_element(By.XPATH, "//a[.//span[@class='a-price']]").click()

driver.find_element(By.CSS_SELECTOR, "input.a-button-input").click()
Actual = driver.find_element(By.ID, 'nav-cart-count').text
Expected = '1'

assert Actual == Expected, f'Expected {Expected}, but we got {Actual}'

print('Test case pass')
driver.quit()

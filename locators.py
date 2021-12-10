from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.chrome()

# Search by ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

driver.find_element(By.XPATH, "//span[@class='icp-nav-flag icp-nav-flag-us']")

# By XPATH with multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

#using contains for partial attributes when an ID is generated as above
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers') and @tabindex='0']")

# Using text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sellers') and @class='nav-a  ']")  # partial text

#Using multiple nodes:
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']/div[@id='nav-xshop']/a[text()='Best Sellers']") # From parent to immediate child
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")  # Parent to grandchildren
# Finding element on dropdown
driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']/option[@value='search-alias=audible']")

# Using only tag
driver.find_element(By.XPATH, "//div")

# Using only attributes
driver.find_element(By.XPATH, "//*[@id='searchDropdownBox']/option[@value='search-alias=audible']")
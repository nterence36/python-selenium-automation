from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()


# Using CSS selector for an element with ID by ID (tag#ID)

driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

# Using classes (tag.class)
driver.find_element(By.CSS_SELECTOR, "span.a-color-state")
driver.find_element(By.CSS_SELECTOR, ".a-color-state")

# 2 or more classes
driver.find_element(By.CSS_SELECTOR, "span.a-color-state.a-text-bold")
driver.find_element(By.CSS_SELECTOR, ".a-color-state.a-text-bold")

# Using attribute
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']")

# Go from parent to children nodes
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='ap_signin_notification_condition_of_use']")

# Class + attributes
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b'][data-csa-c-type='link']")
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers'][data-csa-c-type='link']")
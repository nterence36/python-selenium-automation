from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()

Amazon_logo = driver.find_element(By.CSS_SELECTOR, "i[role='img']")

Create_account = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

Your_name_space = driver.find_element(By.ID, 'ap_customer_name')

Mobile_number-Or-email = driver.find_element(By.ID, 'ap_email')

Password = driver.find_element(By.ID, 'ap_password')

paswords_alert_note = driver.find_element(By.CSS_SELECTOR, "div.a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini")

#password_alert = driver.find_element(By.XPATH, "//div[@class = 'a-box a-alert-inline a-alert-inline-info auth-inlined-information-message a-spacing-top-mini'])

Re-Enter_password_space = driver.find_element(By.ID, 'ap_password_check')

Continue_button = driver.find_element(By.ID, 'continue')

Conditions_Of_Use = driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

Privacy_Notice = driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

Sign-In = driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin']")

Create_A_Free_business_account = driver.find_element(By.ID, 'ab-registration-link')

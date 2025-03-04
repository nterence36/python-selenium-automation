
Amazon_logo = By. Xpath, "//i[@class='a-icon a-icon-logo']"

continue_Button = By.ID, 'continue'

Need_Help_link = By.Xpath, "//span[@class='a-expander-prompt']"

Forget_your_password_link = By.ID, 'auth-fpp-link-bottom'

Other_issues_with-Sign-In_link = By.ID, 'ap-other-signin-issues-link'

Create_your_amazon_account_button = By.ID, 'createAccountSubmit'

Conditions_of_use_link = By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']"

Privacy_Notice_link = By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']"

#Since the conditions of use and privacy notice links contains generated id or information that can be changed
# we can use attributes that looks stable and unique in the link rather than full link as below
Conditions_of_use_link = By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'ap_signin_notification_condition_of_use')]"

Privacy_Notice_link = By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'ap_signin_notification_privacy_notice')]"

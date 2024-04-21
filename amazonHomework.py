from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

sleep(15)
## LOGO AMAZON. search by XPATH
driver.find_element(By.XPATH, "//i[@role='img' and @aria-label='Amazon']")

## EMAIL FIELD. Search by ID
driver.find_element(By.ID, 'ap_email')

## Continue Button. Search by ID
driver.find_element(By.ID, 'continue')

##Conditions of use. Search by XPATH
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

##Conditions of use. Search by XPATH
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

##NEED HELP. Search by Xpath
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

## Forgot your password. Search by Id
driver.find_element(By.ID, "auth-fpp-link-bottom")

## Other Issues with Sign-In. Search by Id
driver.find_element(By.ID, "ap-other-signin-issues-link")

##Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

driver.quit()

Verify SignIn page opened:
“Sign into your Target account” text is shown,
SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

#driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

driver.find_element(By.ID, "search").send_keys("coffee")
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)

#verification
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert 'coffee ' in actual_text , f"ERROR, TEXT COFFEE NOT IN {actual_text}"
print("TEST CASE PASSED")
sleep(22)
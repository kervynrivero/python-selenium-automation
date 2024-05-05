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
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=MCCRBA32GQ3X5W5YND86&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


#homework

#amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

#create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#your name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#email
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#password must be at least
driver.find_element(By.XPATH, "//div[text()= '  Passwords must be at least 6 characters.']")

#reenter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#continue
driver.find_element(By.CSS_SELECTOR, "#continue")

#privacy notic
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_p']")

#condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_c']")

#sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid.pape.max_auth_age=0&openid.r']")
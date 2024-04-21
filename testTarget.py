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
driver.get("https://www.target.com/")

## Click SignIn button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

## Click SignIn from side navigation
sleep(7)
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']").click()

sleep(7)
#Verification
actual_text= driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert 'Sign into your Target account' in actual_text , f"ERROR, TEXT Sign into your Target account NOT IN {actual_text}"
print('TEST PASSED')

element = driver.find_element(By.XPATH, "//span[text()='Sign in with password']").text
assert 'Sign in with password' in element, f"ERROR, TEXT Sign in with password NOT IN {element}"
print('TEST PASSED')

driver.quit()
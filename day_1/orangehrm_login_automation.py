from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window() 
driver.implicitly_wait(10) 

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2) 

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
time.sleep(1.5)

driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
time.sleep(1.5)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(4) 

page_title = driver.title
print("Page title is:", page_title)

if page_title == "OrangeHRM":
    print("Test Passed: Page title is correct.")
else:
    print("Test Failed: Page title is incorrect.")

driver.quit()
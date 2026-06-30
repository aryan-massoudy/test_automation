from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # 2. Create a new instance of the Chrome driver
driver.implicitly_wait(10)  # 1. Set an implicit wait time of 10 seconds


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # 3. Navigate to a webpage

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")  # 4. Find the username field and enter text
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")  # 5. Find the password field and enter text
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # 6. Find the login button and click it      

time.sleep(5)  # 7. Wait for 5 seconds

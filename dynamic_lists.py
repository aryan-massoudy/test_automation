from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # 2. Create a new instance of the Chrome driver
driver.implicitly_wait(10)  # 1. Set an implicit wait time of 10 seconds


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # 3. Navigate to a webpage
time.sleep(2)  # 7. Wait for 5 seconds
driver.maximize_window()  # 4. Maximize the browser window
time.sleep(2)  # 7. Wait for 5 seconds
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")  # 4. Find the username field and enter text
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")  # 5. Find the password field and enter text
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # 6. Find the login button and click it      
time.sleep(5)  # 7. Wait for 5 seconds
driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click() 
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click() 
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click() 

employees = driver.find_elements(By.XPATH, "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-container']/div[@role='table']/div[@role='rowgroup']/div")  # 8. Find all elements with the specified XPath

employees_disabled = 0
for employee in employees:  # 9. Iterate through the list of elements
    if "disabled" in employee.text.lower():  # 10. Check if the text of the element contains the word "disabled"
        employees_disabled += 1

    
print(f"Number of disabled employees: {employees_disabled}")

time.sleep(5)  # 7. Wait for 5 seconds
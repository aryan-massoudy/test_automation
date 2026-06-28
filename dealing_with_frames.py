from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practice-automation.com/iframes/")
time.sleep(2) 
driver.maximize_window()
time.sleep(2) 
driver.switch_to.frame("top-iframe") 
time.sleep(2)  
driver.find_element(By.LINK_TEXT, "Docs").click()  # Click on the "Docs" link
time.sleep(5) 
driver.quit()  # Close the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(4)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
for checkbox in checkboxes:
        if checkbox.get_attribute("id") not in ["saturday", "sunday"]:
                checkbox.click()
                time.sleep(1)
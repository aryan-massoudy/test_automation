from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://practice.expandtesting.com/upload")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='fileInput']").send_keys("C:\\Users\\ARYAN\\Desktop\\test.txt") 

time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='fileSubmit']").click()
time.sleep(10)
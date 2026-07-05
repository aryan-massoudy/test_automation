from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Hello, this is a test input!")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(5)
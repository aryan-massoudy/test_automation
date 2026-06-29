from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium") 
time.sleep(1)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Selenium").click()
driver.find_element(By.LINK_TEXT, "Selenium in biology").click()
driver.find_element(By.LINK_TEXT, "Selenium disulfide").click()
driver.find_element(By.LINK_TEXT, "Selenium (software)").click()
driver.find_element(By.LINK_TEXT, "Selenium dioxide").click()
time.sleep(5)
window_handles = driver.window_handles
for handle in window_handles:
    driver.switch_to.window(handle)
    print("Window title: ", driver.title)   
time.sleep(5)
driver.quit()
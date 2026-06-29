from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
browser_windows = driver.window_handles
parent_window = browser_windows[0]
child_window = browser_windows[1]

driver.switch_to.window(child_window)
print("Child window title: ", driver.title)

driver.switch_to.window(parent_window)
print("Parent window title: ", driver.title)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()


# 1st Method:
driver.execute_script("window.scrollBy(0, 1000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 1000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 1000)")
time.sleep(2)
print("should be 3000: ", driver.execute_script("return window.pageYOffset"))
time.sleep(5)
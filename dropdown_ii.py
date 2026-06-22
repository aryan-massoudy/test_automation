import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.maximize_window()

# Locate the dropdown element
time.sleep(2)
dropdown_element = driver.find_element(By.ID, "country")

# Create a Select object
time.sleep(2)
select_country = Select(dropdown_element)

time.sleep(2)
select_country.select_by_visible_text("Germany")
time.sleep(2)
driver.quit()
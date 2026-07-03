from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.tutorialspoint.com/selenium/practice/slider.php")

intro = driver.find_element(By.XPATH, "//input[@id='ageInputId']")


print("Value before:", intro.get_attribute("value"))
print("Location before:", intro.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(intro, 20, 0).perform()
time.sleep(2)


print("Value after:", intro.get_attribute("value"))
print("Location after:", intro.location)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@id='ez-accept-all']").click()

driver.find_element(By.XPATH, "//textarea[@id='inputText1']").send_keys("Hello World")

actions = ActionChains(driver)
time.sleep(2)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

driver.find_element(By.XPATH, "//textarea[@id='inputText2']").click()

time.sleep(2)
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(5)
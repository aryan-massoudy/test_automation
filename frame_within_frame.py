from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)
outer_frame = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
time.sleep(2)
driver.switch_to.frame(outer_frame)
time.sleep(2)
inner_frame = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
time.sleep(2)
driver.switch_to.frame(inner_frame)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Selenium testing")
time.sleep(2)
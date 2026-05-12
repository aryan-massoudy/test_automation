import time
from selenium import  webdriver
from selenium.webdriver.common.by import By



class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        elem1 = driver.find_element(By.ID,"user-name").send_keys("performance_glitch_user")
        time.sleep(5)
        elem2 = driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(5)
        elem3 = driver.find_element(By.ID,"login-button").click()
        time.sleep(5)


demo_item = DemoFindElementByID()

demo_item.locate_by_id_demo()

import time
from selenium import  webdriver
from selenium.webdriver.common.by import By



class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.mythicsoft.com/filelocatorpro/information/#version-history")
        release_items = driver.find_elements(By.CLASS_NAME,"versionheading")
        for item in release_items:
            print(item.text)



demo_item = DemoFindElementByID()

demo_item.locate_by_id_demo()

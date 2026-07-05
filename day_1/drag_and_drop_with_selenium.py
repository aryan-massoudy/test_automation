import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DemoDragAndDrop():
    def drag_and_drop(self):
        driver = webdriver.Chrome()

        driver.get("https://jqueryui.com/droppable/")

        driver.maximize_window()
        
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        
        time.sleep(2)
        draggable_element = driver.find_element(By.XPATH, "//p[normalize-space()='Drag me to my target']")
        
        time.sleep(2)
        droppable_element = driver.find_element(By.XPATH, "//p[normalize-space()='Drop here']")
        
        time.sleep(2)
        ActionChains(driver).drag_and_drop(draggable_element, droppable_element).perform()

        time.sleep(2)

demo_instnace = DemoDragAndDrop()
demo_instnace.drag_and_drop()
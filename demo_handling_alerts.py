import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoHandlingJsAlerts():
    def hanlde_js_alerts(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
    
        time.sleep(5)
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        
        time.sleep(2)
        driver.switch_to.alert.send_keys("Aryan Massoudy")
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.quit()

demo_instance = DemoHandlingJsAlerts()
demo_instance.hanlde_js_alerts()
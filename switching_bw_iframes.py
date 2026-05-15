import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoSwitchingBwIframes():
    def select_from_iframes(self):
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        time.sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/a[2]").click()
        time.sleep(1)
        
        
demo_instance = DemoSwitchingBwIframes()
demo_instance.select_from_iframes()
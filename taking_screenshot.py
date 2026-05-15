import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoTakingScreenshot:
    def demo_take_screenshot(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(2)
        login_button = driver.find_element(By.CLASS_NAME, "form_column")
        time.sleep(2)
        login_button.screenshot(
            "C:\\Users\\ATHENA\\Documents\\software-testing\\error1.png"
        )
        time.sleep(2)
        login_button2 = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button2.click()
        time.sleep(2)
        login_button.screenshot(
            "C:\\Users\\ATHENA\\Documents\\software-testing\\error2.png"
        )

        time.sleep(2)


demo_item = DemoTakingScreenshot()
demo_item.demo_take_screenshot()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class DemoJS():
    def js_interaction(self):
        driver = webdriver.Chrome()
        driver.execute_script("window.open('https://training.rcvacademy.com/courses','_self')")
        time.sleep(2)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[2];")
        print(demo_element.text)
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(2)

demo_item = DemoJS()
demo_item.js_interaction()
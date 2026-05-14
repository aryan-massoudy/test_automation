import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDropdownSingleSelect():
    def demo_select_drop_down(self):
        driver = webdriver.Chrome()
        driver.get("https://practice.expandtesting.com/dropdown")
        driver.maximize_window()
        time.sleep(2)
        drop_down = driver.find_element(By.ID, "dropdown")
        time.sleep(2)
        select_dropdown = Select(drop_down)
        time.sleep(2)
        select_dropdown.select_by_index(1)
        time.sleep(2)
        select_dropdown.select_by_visible_text("Option 2")
        time.sleep(2)

demo_item = DemoDropdownSingleSelect()
demo_item.demo_select_drop_down()
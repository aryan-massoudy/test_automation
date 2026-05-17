import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
class DemoMouseOver():
    def select_from_dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://dribbble.com/tags/menu-hover")
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)
        explore_dropdown = driver.find_element(By.XPATH, "//a[normalize-space()='Explore']")
        time.sleep(3)
        action_chains = ActionChains(driver)
        time.sleep(3)
        action_chains.move_to_element(explore_dropdown).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@class='site-nav-sub__link'][normalize-space()='Animation']").click()
        time.sleep(3)

demo_instance = DemoMouseOver()
demo_instance.select_from_dropdown()
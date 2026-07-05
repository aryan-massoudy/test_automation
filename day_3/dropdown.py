import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = uc.Chrome(version_main=149)
driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(5)
driver.maximize_window()
time.sleep(2)
dropdown = driver.find_element(By.XPATH, '//*[@id="input-country"]')
Select(dropdown).select_by_visible_text("Germany")
time.sleep(5)
try:
    driver.quit()
except:
    pass


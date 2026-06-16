from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@href='/products']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='search_product']").send_keys("Tshirt")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='submit_search']").click()
time.sleep(2)
list_of_prices = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']//h2")

numeric_prices = []

for item in list_of_prices:
    clean_price = int(item.text.replace("Rs.", "").strip())
    numeric_prices.append(clean_price)
print(f"Highest Price: Rs. {max(numeric_prices)}")
print(f"Lowest Price: Rs. {min(numeric_prices)}")
time.sleep(2)

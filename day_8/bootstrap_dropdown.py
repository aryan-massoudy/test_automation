from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

countries_dropdown = driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']")

driver.execute_script("arguments[0].scrollIntoView()", countries_dropdown)

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

for country in countries_list:
    print(country.text)
    if country.text == "India":
        country.click()
        break


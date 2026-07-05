from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(2)
 
driver.find_element(By.XPATH, '//*[@id="product_551"]').click() 
driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Aryan")
driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Massoudy")

driver.find_element(By.XPATH, "//input[@id='dob']").click()

dobmonth_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
dobmonth_select.select_by_visible_text("Jan")

dobyear_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
dobyear_select.select_by_visible_text("1993")

dob_select = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for date in dob_select:
    if date.text == "15":
        date.click()
        break


driver.find_element(By.XPATH, "//input[@id='sex_1']").click()
driver.find_element(By.XPATH, "//input[@id='traveltype_2']").click()    
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Berlin")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Hurghada") 



driver.find_element(By.XPATH, "//input[@id='departon']").click()

dep_month_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
dep_month_select.select_by_visible_text("Dec")

dep_year_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
dep_year_select.select_by_visible_text("2026")

dep_date_select = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for date in dep_date_select:
    if date.text == "20":
        date.click()
        break




driver.find_element(By.XPATH, "//input[@id='returndate']").click()

rtn_year_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
rtn_year_select.select_by_visible_text("2027")

rtn_month_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
rtn_month_select.select_by_visible_text("Jan")


rtn_date_select = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for date in rtn_date_select:
    if date.text == "10":
        date.click()
        break

time.sleep(10)

# 1. Click the custom dropdown container to open the options list
driver.find_element(By.XPATH, "//span[@id='select2-reasondummy-container']").click()

time.sleep(1) # Give the dropdown list a brief moment to animate open


driver.find_element(By.XPATH, '//li[contains(text(), "Prank a friend")]').click()

driver.find_element(By.XPATH, "//input[@id='deliverymethod_3']").click()

driver.find_element(By.XPATH, "//input[@id='billname']").send_keys("Aryan Massoudy")
driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("aryan_massoudy@example.com")

driver.find_element(By.XPATH, "//span[@aria-label='Country']//b[@role='presentation']").click()
driver.find_element(By.XPATH, '//li[contains(text(), "Germany")]').click()

driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("Musterstrasse 1")
driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("28")
driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("13798")
driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Berlin")

driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']").click()
driver.find_element(By.XPATH, '//li[contains(text(), "Berlin")]').click()


driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("+49123456789")

time.sleep(2)

price_shown = driver.find_element(By.XPATH, "//li[3]//span[2]//span[1]//bdi[1]").text

total_price = driver.find_element(By.XPATH, "//tr[contains(@class,'order-total')]//bdi[1]").text

if price_shown == total_price:
    print("Test passed. The prices are matching.")
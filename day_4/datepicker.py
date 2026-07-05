from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
# driver.implicitly_wait(10)  
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()  # Maximize the browser window 


driver.switch_to.frame(0)

year = "1993"
month = "January"
date = "15"

driver.find_element(By.ID, "datepicker").click()


while True:
    selected_month = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    selected_year = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    if selected_month == month and selected_year == year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
        
        
day_elements = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for day in day_elements:
    if day.text == date:
        day.click()
        break


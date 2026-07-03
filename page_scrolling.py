from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(2)
driver.maximize_window()


# 1st Method:
# driver.execute_script("window.scrollBy(0, 1000)")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 1000)")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 1000)")
# time.sleep(2)
# print("should be 3000: ", driver.execute_script("return window.pageYOffset"))
# time.sleep(5)


# 2nd Method:
# germany_flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Germany']")
# driver.execute_script("arguments[0].scrollIntoView()", germany_flag)
# time.sleep(5)

# 3rd Method:
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)
print("Top of of the page: ", driver.execute_script("return window.pageYOffset"))


driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
print("Bottom of page: ", driver.execute_script("return window.pageYOffset"))
time.sleep(5)
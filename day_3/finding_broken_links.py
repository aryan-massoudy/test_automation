from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
time.sleep(1)
driver.maximize_window()
time.sleep(1)
links = driver.find_elements(By.TAG_NAME, "a")
print("Total links are: ", len(links))

count = 0

for link in links:
    try:
        url = link.get_attribute("href")
    except:
        print("Exception occurred for link: ", link)
        continue
    if not url or not url.startswith("http"):
        continue
    try:
        response = requests.head(url, timeout=5)
    except requests.RequestException as e:
        print("Request failed for:")
        print('-----------------------------------------')
        print(url)
        print('-----------------------------------------')
        print(e)
        print('-----------------------------------------')
        continue
    if response.status_code >= 400:
        print(url, "is a broken link")
        count += 1
    else:
        print(url, "is a valid link")
print("Total broken links are: ", count)
driver.quit()
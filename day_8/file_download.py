from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

location = os.getcwd()


def chrome_driver():
    preferences = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True,
        # "download.prompt_for_download": False,    
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=options)
    return driver

driver = chrome_driver()
driver.implicitly_wait(10)

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-top"]/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p').click()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(5)
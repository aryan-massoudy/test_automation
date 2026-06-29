from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 1. Import Options


chrome_options = Options()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--window-size=1920,1080") 

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

number_of_rows = len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr"))
number_of_columns = len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr/th"))

for row in range(2, number_of_rows + 1):
    author_name = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr[" + str(row) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr[" + str(row) + "]/td[1]").text
        print("Book name of author Mukesh is: " + book_name)
print() 
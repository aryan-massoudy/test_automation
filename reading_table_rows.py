import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start the browser
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

# Open the CSV file to save data
file = open("book_table_data.csv", mode="w", newline="", encoding="utf-8")
writer = csv.writer(file)

# Find all the rows in the table
table_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")

for row in table_rows:
    # if row == table_rows[0]:  # Skip the header row 
    #     continue
    # Create an empty list to hold the data for the current row
    row_data = []
    
    # Find all the table cells (td) inside this specific row
    cells = row.find_elements(By.XPATH, "./th | ./td")  # Use 'td' for data cells and 'th' for header cells
    
    # Loop through each cell to grab the text
    for cell in cells:
        text_inside_cell = cell.text
        row_data.append(text_inside_cell) # Add the text to our row list
        
    # Write the completed row list to the CSV file
    print("Row data: ", row_data)  # Optional: Print the row data to console for verification
    writer.writerow(row_data)

# Clean up and close everything
file.close()
driver.quit()

print("Data successfully saved to 'book_table_data.csv'!")
import csv


with open('book_table_data.csv', mode='r', newline='', encoding='utf-8' ) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
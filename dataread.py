import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Gets the first line
    print(headers)


# Rename file uploaded to "data" in order for it to read the csv file

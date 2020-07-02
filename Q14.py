# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.

import csv


def csv_read():
    with open("peoples_record.csv", 'r') as file:
        for line in csv.DictReader(file):
            print(dict(line))


csv_read()

import csv

with open("data/flights.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
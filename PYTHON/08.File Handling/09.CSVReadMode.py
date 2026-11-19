import csv

with open("CSVFile.csv","r") as f:
    data = csv.reader(f)
    for i in data:
        print(i)
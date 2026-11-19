import csv

with open("CSVFile.csv","w",newline="") as f:
    x = csv.writer(f)
    x.writerow(["Name","City"])
    x.writerow(["Yash Kumar","Vaishali"])
    x.writerow(["Kumar","Noida"])


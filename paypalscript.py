#!/usr/bin/env python3
import csv

mapping = {"Date": "Date", "Name": "Name", "Amount": "Net", "Description": "Type"}

def strip_row(row):
    return {k: row[v] for k,v in mapping.items()}

with open("Paypal Export.csv", 'r') as filein:
    csv_filein = [strip_row(row) for row in csv.DictReader(filein) if row["Balance Impact"] == "Credit"]
    with open('output.csv', 'w', newline='') as fileout:
        writer = csv.DictWriter(fileout, fieldnames=mapping.keys())
        writer.writeheader()
        [writer.writerow(row) for row in csv_filein]
        fileout.close()
    filein.close()

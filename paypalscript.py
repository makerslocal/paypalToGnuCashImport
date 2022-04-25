#!/usr/bin/env python3
import csv

mapping = {"Date": "Date", "Name": "Name", "Amount": "Net", "Description": "Type"}

def strip_row(row):
    return {k: row[v] for k,v in mapping.items()}

with open("Paypal Export.csv", 'r', encoding="utf-8-sig") as filein:
    csv_filein = [strip_row(row) for row in csv.DictReader(filein) if row["Balance Impact"] == "Credit"]
    with open('output.csv', 'w', newline='') as fileout:
        writer = csv.DictWriter(fileout, fieldnames=mapping.keys())
        writer.writeheader()
        writer.writerows(csv_filein)

#!/usr/bin/env python3
import argparse
import csv
import os.path

#
# Parse and set Input and Output Files
#

parser = argparse.ArgumentParser(description='Takes a PayPal CSV export file and generates a GnuCash formatted CSV import file.  Default input file name is Paypal Export.csv.  Defaults output file name is output.csv')
parser.add_argument('-i','--input', help='Input file name',required=False)
parser.add_argument('-o','--output',help='Output file name', required=False)
args = parser.parse_args()

inputFile = args.input
if not bool(inputFile):
    inputFile = 'Paypal Export.csv'

if not os.path.exists(inputFile.strip('\n')):
    print("Input file does not exist: " + inputFile)
    quit()

print("Input File:  " + inputFile)    

outputFile = args.output
if not bool(outputFile):    
    outputFile = "Output.csv"

print("Output File: " + outputFile)

#
# Parse input file and create output file
#

mapping = {"Date": "Date", "Name": "Name", "Amount": "Net", "Description": "Type"}

def strip_row(row):
    return {k: row[v] for k,v in mapping.items()}

with open(inputFile, 'r', encoding="utf-8-sig") as filein:
    csv_filein = [strip_row(row) for row in csv.DictReader(filein) if row["Balance Impact"] == "Credit"]
    with open(outputFile, 'w', newline='') as fileout:
        writer = csv.DictWriter(fileout, fieldnames=mapping.keys())
        writer.writeheader()
        [writer.writerow(row) for row in csv_filein]
        fileout.close()
    filein.close()



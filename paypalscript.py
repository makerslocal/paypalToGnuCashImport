#!/usr/bin/env python3
import argparse
import csv
import os.path

#
# Parse and set Input and Output Files
#

parser = argparse.ArgumentParser(description='Takes a PayPal CSV export file and generates a GnuCash formatted CSV import file.  Default input file name is Paypal Export.csv.  Defaults output file name is output.csv')
parser.add_argument('-i','--input', help='Input file name', nargs="?", default="Paypal Export.csv", type=str)
parser.add_argument('-o','--output',help='Output file name', nargs="?", default="Output.csv", type=str)
args = parser.parse_args()

inputFile = args.input

if not os.path.exists(inputFile.strip('\n')):
    print("Input file does not exist: " + inputFile)
    quit()

print("Input File:  " + inputFile)    

outputFile = args.output
print("Output File: " + outputFile)

#
# Parse input file and create output file
#


class PayPalConverter:
    """
    Parses Paypal csv files into something GNUCash can read
    """
    data = []
    mapping = {'Date': 'Date', 'Name': 'Name', 'Amount': 'Net', 'Description': 'Type'}
    paypal_header = 'Balance Impact'
    balance_type = 'Credit'

    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file

    def _strip_row(self, row):
        return {k: row[v] for k, v in self.mapping.items()}

    def read(self):
        try:
            with open(self.in_file, 'r', encoding='utf-8-sig') as f:
                self.data = [self._strip_row(row) for row in csv.DictReader(f) if row[self.paypal_header] ==
                             self.balance_type]
        except FileNotFoundError:
            exit(f"File { self.in_file } not found")

    def write(self):
        with open(self.out_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.mapping.keys())
            writer.writeheader()
            writer.writerows(self.data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Takes a PayPal CSV export file and generates a GnuCash formatted CSV '
                                                 'import file.  Default input file name is Paypal Export.csv.  '
                                                 'Defaults output file name is Output.csv')
    parser.add_argument('-i', '--input', default='Paypal Export.csv', help='Input file name')
    parser.add_argument('-o', '--output', default='Output.csv', help='Output file name')
    args = parser.parse_args()

    print(f'Input File: { args.input }')
    print(f'Output File: { args.output }')

    # Parse input file and create output file
    converter = PayPalConverter(in_file=args.input, out_file=args.output)
    converter.read()
    converter.write()

import csv
ldate = ["Date"]
lname = ["Name"]
lammo = ["Ammount"]
ldesc = ["Description"]
with open("Paypal Export.CSV", 'r', encoding="utf-8-sig") as filein:
    csv_filein = csv.DictReader(filein)
    for rowi in csv_filein:
        if rowi["Balance Impact"] == "Credit":
            ldate.append(rowi["Date"])
            lname.append(rowi["Name"])
            lammo.append(rowi["Net"])
            ldesc.append(rowi["Type"])
    filein.close()


with open('output.csv', 'w', newline='') as fileout:
    writer = csv.writer(fileout)
    rcount = 0
    for row in ldate:
        writer.writerow((ldate[rcount], lname[rcount], lammo[rcount], ldesc[rcount]))
        rcount = rcount + 1
    fileout.close()

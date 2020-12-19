import csv
def getCSVdata(filename):
    rows = []
    filedata = open(filename, mode = "r")
    # create CSV Reader from CSV file
    reader = csv.reader(filedata)
    # skip the header in CSV file
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
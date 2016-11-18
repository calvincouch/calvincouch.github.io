import csv
data = csv.reader(open('DAT_ASCII_USDJPY_M1_201610.CSV'))
# Read the column names from the first line of the file
fields = data.next()
for row in data:
        # Zip together the field names and values
    items = zip(fields, row)
    item = {}
        # Add the value to our dictionary
    for (name, value) in items:
        item[name] = value.strip()

print item	

data.close

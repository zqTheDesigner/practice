#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFileName in os.listdir('.'):
	if not csvFileName.endswith('.csv'):
		continue

	print('Removing header from ' + csvFileName + '...')

	# Read the csv file in (skipping first row)
	csvRows = []
	csvFileObj = open(csvFileName)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # Skip first row
		csvRows.append(row)
	csvFileObj.close()

	#TODO: Write out the csv file
	csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()


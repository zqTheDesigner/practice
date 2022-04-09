#! Python3
# renameDate.py - Renames filenames with american MM-DD-YYYY date format
# to European DD-MM-YY

import shutil, os, re

# Create a regeg that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
	((0|1)?\d)- #One or two digit for the month
	((0|1|2|3)?\d)- # One or two digits for the day
	((19|20)\d\d) #four digits for the year
	(.*?)$
""", re.VERBOSE)

# TODO loop over the files in the working directory
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)
	# TODO Skip files without a date
	if mo == None:
		print('no-match')
		continue
	# TODO Get the different part of the filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPat = mo.group(8)

# TODO Form the European-style filename
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPat
	absWorkingDir = os.path.abspath('./')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	print(f'renaming "{amerFilename}" to "{euroFilename}" ...')
	shutil.move(amerFilename, euroFilename) # Uncomment after testing

# TODO: Get the full absolute file path

# TODO rename the files
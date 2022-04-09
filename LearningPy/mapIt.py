#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command lone or clipboard

import webbrowser, sys, pyperclip

import pyperclip
if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard
else:
	address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address)
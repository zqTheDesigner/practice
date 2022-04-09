#! Python 3
# mcp.pyw - Saves and load pieces of text to the clipboard
# Usage: py mcb.pyw save <keyword> - saves clipboard to keyword
#        py mcb.pyw <keyword> - loads keywords to clipboard
#        py mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2 :
# TODO List keywords and load content
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

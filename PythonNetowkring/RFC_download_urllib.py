#! python3

import sys, urllib.request

try:
	rfc_number = int(sys.argv[1])
except:
	print('Must supply an RFC number')
	sys.exit(2)

template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
url = template.format(rfc_number)

rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()

print(rfc)
#! python3

import sys, socket

try:
	rfc_number = int(sys.argv[1])
except:
	print('Must supply an RFC number')
	sys.exit(2)

host = 'www.rfc-editor.org'
port = 80

# Tell socket which transport layer we want to use
socket = socket.create_connection((host, port))

req = ('GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
'Host: {host}:{port} \r\n'
'User-Agent: Python {version}\r\n'
'Connection: close\r\n'
'\r\n'
)

req = req.format(rfcnum = rfc_number, host=host, port=port, version=sys.version_info[0])

# Data that sent through TCP. Muust be raw bytes, use ascii to encode
socket.sendall(req.encode('ascii'))
rfc_bytes = bytearray()

while True:
	buf = socket.recv(4096)

	# The recv() call will return empty string after the server sends all of its data and close the connection
	if not len(buf):
		break
	rfc_bytes += buf
rfc = rfc_bytes.decode('utf-8')

print(rfc)


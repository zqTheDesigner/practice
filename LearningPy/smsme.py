#! python3
# smsme.py - Send Text message to myself via command line

import sys

if len(sys.argv) < 2:
	print('2nd Argument required')
	exit()

message = sys.argv[1]

# Preset values:
accountSID = 'ACc3aaef10cf9d2aaf92bec2c029167bd4'
authToken = 'fd999c76af82f4b71e5d3186a8fbe5db'
myTwilioNum = '+17692070713'
myNum = '+6590697196'

from twilio.rest import Client
def textMyself(message):
	twilioCli = Client(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=myTwilioNum, to=myNum)

textMyself(message)

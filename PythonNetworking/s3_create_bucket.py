from heapq import nsmallest
import xml.etree.ElementTree as ET

import requests
import requests_aws4auth

auth = requests_aws4auth.AWS4Auth('AKIAYYL3NTNTZQ4BOVM2','WyG9+rm6io1ldhKicbjXhUwiXQG+dTZMfnS+pUtq','ap-southeast-1','s3')

ns = 'https://s3.amazonaws.com/doc/2006-03-01'

def create_bucket(bucket):
	print(bucket)
	XML = ET.Element('CreateBucketConfiguration')
	XML.attrib['xmlns'] = ns
	location = ET.SubElement(XML, 'LocationConstraint')
	location.text = auth.region
	data = ET.tostring(XML, encoding='utf-8')
	endpoint = 's3.ap-southeast-1.amazonaws.com'
	url = 'http://{}.{}'.format(bucket, endpoint)
	xml_pprint(data)
	response = requests.put(url, data=data, auth = auth)
	print(response)
	if response.ok:
		print('Created bucket{} ok'.format(bucket))
	else:
		xml_pprint(response.text)

import xml.dom.minidom as minidom
def xml_pprint(xml_string):
	print(minidom.parseString(xml_string).toprettyxml())


create_bucket('testbucketzqthedesigner')

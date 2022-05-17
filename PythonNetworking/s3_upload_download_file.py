import requests
import requests_aws4auth

auth = requests_aws4auth.AWS4Auth('AKIAYYL3NTNTZQ4BOVM2','WyG9+rm6io1ldhKicbjXhUwiXQG+dTZMfnS+pUtq','ap-southeast-1','s3')

endpoint = 's3.ap-southeast-1.amazonaws.com'

def upload_file(bucket, local_path):
	data = open(local_path, 'rb').read()
	url = 'http://{}/{}/{}'.format(endpoint, bucket, local_path)
	print('upload file ' + url)
	response = requests.put(url, data = data, auth = auth)
	if response.ok:
		print('Upload {} OK'.format(local_path))
	else:
		xml_pprint(response.text)


import xml.dom.minidom as minidom
def xml_pprint(xml_string):
	print(minidom.parseString(xml_string).toprettyxml())


# upload_file('testbucketzqthedesigner', './README.md')

def download_file(bucket, local_path):
	s3_name = 'README.md'
	url = 'http://{}/{}/{}'.format(endpoint, bucket, s3_name)
	print('Download file ' + url)
	response = requests.get(url, auth = auth)
	print(response)
	if response.ok:
		open('testtest', 'wb').write(response.content)
		print('Downalod {} OK'.format(s3_name))
	else:
		xml_pprint(response.text)

download_file("testbucketzqthedesigner",'README.md')

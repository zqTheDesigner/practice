#! python3

import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys
import os

response = requests.get('http://www.freeimages.co.uk/galleries/transtech/informationtechnology/index.htm')

parse = BeautifulSoup(response.text, 'lxml')

# Get all image tags
image_tags = parse.find_all('img')

# Get urls to the images
images = [ url.get('src') for url in image_tags]

# If no image found in the page
if not images :
		sys.exit('Found no images')
	
images = [urllib.parse.urljoin(response.url, url) for url in images]
print('Found %s images' % len(images))

# Create download_images folder if not exists
file_path = 'download_images'
directory = os.path.dirname(file_path)

if not os.path.exists(directory):
	try:
		os.makedirs(file_path)
		print('Creation of the directory %s OK' % file_path)
	except OSError:
		print('Creation of the directory %s failed' % file_path)
else:
	print('%s directory exists' % file_path)

# Download images to downloaded folder
for url in images:
	response = requests.get(url)
	file = open('download_images/%s' % url.split('/')[-1], 'wb')
	file.write(response.content)
	file.close()
	print('Downloaded %s' % url)


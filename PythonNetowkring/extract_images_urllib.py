#! python3

from urllib.request import urlopen, urljoin
import re

def download_page(url):
	page = urlopen(url).read().decode('utf-8')
	print(page)
	return page

def extract_image_locations(page):
	img_regx = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
	return img_regx.findall(page)

url = 'https://en.wikipedia.org/wiki/Wikipedia'
packtpub = download_page(url)
image_locations = extract_image_locations(packtpub)

print(image_locations)

for src in image_locations:
	print(urljoin(url, src))
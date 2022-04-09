#! python3

from html.parser import HTMLParser
import urllib.request
class myParser(HTMLParser):
	print(HTMLParser)
	def handle_starttag(self, tag, attrs):
		if(tag=='a'):
			for a in attrs:
				if(a[0] == 'href'):
						link = a[1]
						print(link)
						newParse = myParser()

url = 'https://en.wikipedia.org/wiki/Main_Page'
request = urllib.request.urlopen(url)
parser = myParser()
parser.feed(request.read().decode('utf-8'))
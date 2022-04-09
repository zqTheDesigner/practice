#! python3
# searchpypi.py - Open serveral search results.

import requests, sys, webbrowser, bs4

print('Searching...','https://pypi.org/search?q=' + ''.join(sys.argv[1]) )
res = requests.get('https://pypi.org/search?q='+ ''.join(sys.argv[1]))
res.raise_for_status()

# TODO: Retrive top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# TODO Open a browser tab for each result
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
	urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
	print('Opening', urlToOpen)
	webbrowser.open(urlToOpen)
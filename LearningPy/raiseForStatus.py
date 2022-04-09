import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
	res.raise_for_status()
except Exception as exc:
	print(exc)

playFile = open('rj.txt', 'w')
# for chunk in res.iter_content(100000):
	# playFile.write(chunk)
playFile.write(res.text)
playFile.close()
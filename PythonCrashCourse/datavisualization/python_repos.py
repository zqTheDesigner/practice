import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept':'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)

print(f'Status code: {r.status_code}')

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']

# Examine the first repository
repo_dict = repo_dicts[0]
repo_links, stars, labels = [],[], []

print("\n Selected information about each repository:")
for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	stars.append(repo_dict['stargazers_count'])
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner} <br />{description}"
	labels.append(label)
	print(f"\nName: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Description: {repo_dict['description']}")

# Make visualization
data = [{
	'type':'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker':{
		'color': 'rgb(60,100,150)',
		'line': {
			'width': 1.5,
			'color': 'rgb(25,25,25)'
		},
		'opacity': 0.6
	}
}]

my_layout = {
	'title': "Most-Starred Pytjon Projects on Github",
	'titlefont': {'size': 28},
	'xaxis': {'title':'Repository', 'tickfont':{'size': 14}},
	'yaxis': {'title':"Stars", 'tickfont':{'size': 14}},
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='python_repos.html')
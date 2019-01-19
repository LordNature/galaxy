import requests, json, collections

# Fetches Kitsu API
def fetch_user(username):
	response = requests.get(
		'https://kitsu.io/api/edge/users?filter[name]=' + username,
		headers = {
			'Content-Type': 'application/vnd.api+json',
			'Accept': 'application/vnd.api+json'
		})
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))['data'][0]
	else:
		return None

# Converts minutes to readable format
def mins_to_string(mins):
	# ORDERED list
	date = [
		('year', 525600),
		('month', 43200),
		('day', 1440),
		('hour', 60),
		('minute', 1)
	]

	date = collections.OrderedDict(date)

	result = []
	for name in date:
		time = mins // date[name]
		if time == 1:
			result.append(str(time) + " " + name)
		elif time >= 2:
			result.append(str(time) + " " + name + "s")
		mins %= date[name]
	return result

def watch_data(id):
	response = requests.get(
		'https://kitsu.io/api/edge/users/' + id + '/library-entries?filter[status]=current&page[limit]=5&page[offset]=0',
		headers = {
			'Content-Type': 'application/vnd.api+json',
			'Accept': 'application/vnd.api+json'
		})
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

def anime_data(anime_id):
	response = requests.get(
		'https://kitsu.io/api/edge/library-entries/' + anime_id + '/anime',
		headers = {
			'Content-Type': 'application/vnd.api+json',
			'Accept': 'application/vnd.api+json'
		})
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))['data']['attributes']
	else:
		return None	
		
latest = []
def parse_anime(kitsuID):
	global latest

	if not latest:
		watchlist = watch_data(kitsuID)['data']
		for anime in watchlist:
			attr = anime_data(anime['id'])
			latest.append({
					'title': attr['canonicalTitle'],
					'episodes_watched': anime['attributes']['progress'],
					'episodes': attr['episodeCount'],
					'last_watched': anime['attributes']['updatedAt'],
					'img': attr['posterImage']['original'],
					'slug': attr['slug']
				})
	return latest
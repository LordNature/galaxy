import requests, json, collections

# Fetches Kitsu API
def fetchUser(username):
	response = requests.get(
		'https://kitsu.io/api/edge/users?filter[name]=' + username,
		headers = {
			'Content-Type': 'application/vnd.api+json',
			'Accept': 'application/vnd.api+json'
		})
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

# Converts minutes to readable format
def minsToString(mins):
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
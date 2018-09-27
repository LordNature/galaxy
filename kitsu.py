import requests, json

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

def minsToString(mins):
	dateTypes = {
		'year': 525600, # 24*60*365
		'month': 43200, # 24*60*30
		'day': 1440, # 24*60
		'hour': 60,
		'minute': 1
	}
	result = []

	# I obviously broke something in this.
	for types in dateTypes:
		time = mins // dateTypes[types]
		if time == 0:
			result.append(time)
		elif time == 1:
			result.append(" " + str(time) + " " + types)
		elif time >= 2:
			result.append(" " + str(time) + " " + types + "s")
		mins %= dateTypes[types]
	return result
# Fetches Youtube API music and displays from text array
import random

def fetchLine(fileName):
	with open(fileName, 'r') as f:
		# Initiaizes vars in rare case of missing declaration on return
		line = next(f)
		randLine = line
		for count, line in enumerate(f, 1):
			if random.randrange(count): continue
			randLine = line
		return randLine
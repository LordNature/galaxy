# Fetches Youtube API music and displays from text array
import random

def fetchVideo():
	with open('static/videos.txt', 'r') as f:
		music = f.readlines()
	return random.choice(music)

# Less efficient?
def fetchPhraseOld():
	with open('static/phrase.txt', 'r') as f:
		phrase = f.readlines()
	return random.choice(phrase)

# More efficient?
def fetchPhrase():
	with open('static/phrase.txt', 'r') as f:
		for count, line in enumerate(f, 2):
			if random.randrange(count): continue
			phrase = line
		return phrase

# simplify both into one function
def fetchLine(fileName):
	with open(fileName, 'r') as f:
		# Initiaizes vars in rare case of missing declaration on return
		line = next(f)
		randLine = line
		for count, line in enumerate(f, 1):
			if random.randrange(count): continue
			randLine = line
		return randLine
# Fetches Youtube API music and displays from text array
import random

def fetchVideo():
	with open('static/videos.txt', 'r') as f:
		music = f.readlines()
	return random.choice(music)

def fetchPhrase():
	with open('static/phrase.txt', 'r') as f:
		phrase = f.readlines()
	return random.choice(phrase)
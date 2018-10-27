# Init file for gala
from flask import Flask, render_template
from kitsu import *
from music import *
import time, subprocess, re


app = Flask(__name__)
year = time.strftime('%Y')

@app.route('/')
def home():
	with open('static/pi.txt', 'r') as f:
		pi = f.read()
	uptime = subprocess.check_output('uptime -p', shell=True)
	# RegEx
	uptime = re.findall(r"'(.*?)\\n'", str(uptime))[0]
	return render_template('home.html', year=year, pi=pi, uptime=uptime)

@app.route('/anime')
def anime():
	kitsu = fetchUser('Nature')['data'][0]
	totalAnime = minsToString(kitsu['attributes']['lifeSpentOnAnime'])
	return render_template('anime.html', year=year, kitsu=kitsu, totalAnimeTime=totalAnime)

@app.route('/music')
def music():
	return render_template('music.html', music=fetchVideo(), oblivion=fetchPhrase())

if __name__ == '__main__':
	app.run(debug=True)
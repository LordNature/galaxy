# Init file for gala
from flask import Flask, render_template
from kitsu import *
import time, subprocess, re


app = Flask(__name__)

@app.route('/')
def home():
	with open('static/pi.txt', 'r') as f:
		pi = f.read()
	uptime = subprocess.check_output('uptime -p', shell=True)
	uptime = re.findall(r"'(.*?)\\n'", str(uptime))[0]
	return render_template('home.html', year=time.strftime('%Y'), pi=pi, uptime=uptime)

@app.route('/anime')
def anime():
	kitsu = fetchUser('Nature')['data'][0]
	totalAnime = minsToString(kitsu['attributes']['lifeSpentOnAnime'])
	return render_template('anime.html', kitsu = kitsu, totalAnimeTime = totalAnime)

if __name__ == '__main__':
	app.run(debug=True)
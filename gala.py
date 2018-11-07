# Init file for gala
from flask import Flask, render_template
import kitsu, file
import time, subprocess, re


app = Flask(__name__)
year = time.strftime('%Y')

# Anime
kitsuData = kitsu.fetchUser('Nature')['data'][0]
totalAnime = kitsu.minsToString(kitsuData['attributes']['lifeSpentOnAnime'])

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
	return render_template('anime.html', year=year, kitsu=kitsu, totalAnimeTime=totalAnime)

@app.route('/music')
def music():
	return render_template('music.html', music=file.fetchLine('static/videos.txt'), oblivion=file.fetchLine('static/phrase.txt'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
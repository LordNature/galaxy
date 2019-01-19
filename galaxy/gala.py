"""
gala.py
-------
Handles all pages and redirects for now
"""

import subprocess, re
# Flask blueprinting services
from flask import (
	Blueprint, flash, g, redirect, render_template, url_for, abort
)

from galaxy.kitsu import *
from galaxy.file import *

bp = Blueprint('gala', __name__)
#year = time.strftime('%Y')

# Index
@bp.route('/')
def index():
	with open('galaxy/static/pi.txt', 'r') as f:
		pi = f.read()
	uptime = subprocess.check_output('uptime -p', shell=True)
	uptime = re.findall(r"'(.*?)\\n'", str(uptime))[0] # RegEx
	return render_template('index.html', pi=pi, uptime=uptime)

# Anime list
@bp.route('/anime')
def anime():
	error = None
	
	try:
		kitsu_data = fetch_user('Nature')
		total_anime = mins_to_string(kitsu_data['attributes']['lifeSpentOnAnime'])
		watchlist = parse_anime(kitsu_data['id'])
	except IndexError:
		kitsu_data = None
		total_anime = None

	if kitsu_data is None:
		error = 'Kitsu API unreachable.'
		flash(error)
		abort(500)

	return render_template('anime.html', kitsu=kitsu_data, totalAnimeTime=total_anime, watchlist=watchlist)

# Music area
@bp.route('/music')
def music():
	return render_template('music.html', music=fetch_line('galaxy/static/videos.txt'), oblivion=fetch_line('galaxy/static/phrase.txt'))

# Aersia music
@bp.route('/vip')
def vip():
	return render_template('vip.html')
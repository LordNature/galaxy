# Init file for gala
from flask import Flask, render_template
import time, subprocess, re

app = Flask(__name__)

@app.route('/')
def home():
	with open('app/static/pi.txt', 'r') as f:
		pi = f.read()
	#b'up 1 day, 21 hours, 48 minutes\n'
	uptime = subprocess.check_output('uptime -p', shell=True)
	uptime = re.findall(r"'(.*?)\\n'", str(uptime))[0]
	return render_template('home.html', year=time.strftime('%Y'), pi=pi, uptime=uptime)

if __name__ == '__main__':
	app.run(debug=True)
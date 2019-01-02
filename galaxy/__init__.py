# INIT file for Galaxy.moe
import os

from flask import Flask, render_template
from . import gala, kitsu, file

def create_app(test_config=None):
	app = Flask(__name__)

	@app.errorhandler(404)
	def not_found(error):
		return render_template('404.html'), 404

	# Calls gala.py and initializes the blueprint
	# Read more: http://flask.pocoo.org/docs/1.0/blueprints/
	app.register_blueprint(gala.bp)
	app.add_url_rule('/', endpoint='index')

	return app
# INIT file for Galaxy.moe
import os, time
from flask import Flask, render_template
from galaxy import gala, kitsu, file

def create_app(test_config=None):
	# Creates & configs
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev', # randomize this in production
	)

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	@app.context_processor
	def inject_year():
		return dict(year=time.strftime('%Y'))

	@app.errorhandler(404)
	def not_found(error):
		return render_template('404.html'), 404

	@app.errorhandler(500)
	def not_found(error):
		return render_template('500.html'), 500

	# Calls gala.py and initializes the blueprint
	# Read more: http://flask.pocoo.org/docs/1.0/blueprints/
	app.register_blueprint(gala.bp)
	app.add_url_rule('/', endpoint='index')
	
	return app
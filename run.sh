#!/bin/sh
export FLASK_APP=gala.py
#export FLASK_ENV=production
export FLASK_ENV=development
exec flask run

#!/bin/sh
export FLASK_APP=gala.py
export FLASK_ENV=production
exec flask run

# api.py
# Handles all API requests for screenshot service

import boto3, botocore, os
from flask import current_app as app
from flask import abort
from werkzeug.utils import secure_filename

def auth_check(request):
	try:
		file_name = os.path.join(app.instance_path, 'accounts.txt')

		with open(file_name, 'r') as f:
			auth_keys = f.readlines()
		f.closed

		for user in auth_keys:
			user = user.strip('\n').split(':')
			if (request.form['user'] == user[0] and request.form['key'] == user[1]):
					return True
	except Exception as e:
		return e

def upload_s3(file, user):
	s3 = boto3.client(
		's3',
		aws_access_key_id=app.config['S3_KEY'],
		aws_secret_access_key=app.config['S3_SECRET']
	)

	filename = secure_filename(file.filename)

	s3.upload_fileobj(
		file,
		app.config['S3_BUCKET'],
		user + '/' + filename,
		ExtraArgs={
			'ACL': 'public-read',
			'ContentType': file.content_type
		}
	)
	return 'http://{}.s3.amazonaws.com/{}/{}'.format(app.config['S3_BUCKET'], user, filename)
"""
John Doe's Flask API.
"""

from flask import Flask, abort, send_from_directory

import os

import configparser

app = Flask(__name__)

def parse_config(config_paths):

    config_path = None

    for f in config_paths:

        if os.path.isfile(f):

            config_path = f

            break

    if config_path is None:

        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()

    config.read(config_path)

    return config

@app.route("/<string:msg>")

def greetings(msg):

	if (".." in msg) or ("~" in msg):

		abort(403)

	else:

		if os.path.isfile(f"./pages/{msg}"):

			return send_from_directory('./pages', msg), 200

		else:

			abort(404)

@app.errorhandler(403)

def forbidden(e):

	return send_from_directory('./pages', '403.html'), 403

@app.errorhandler(404)

def not_found(e):

	return send_from_directory('./pages', '404.html'), 404

if __name__ == "__main__":

	config = parse_config(["credentials.ini", "default.ini"])

	message_port = config["SERVER"]["PORT"]

	message_debug = config["SERVER"]["DEBUG"]

	app.run(debug=message_debug, host='0.0.0.0', port=message_port)

from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS

try: 
	import mysql.connector
except: 
	print("No sql connection")
import bcrypt
import json

try:
	import ai_logic as ai
	print("Is ai yes")
	noai = False
except:
	print("Ai not working")
	noai = True


app = Flask(
    __name__,
    template_folder='../SRC/HTML/',
    static_folder='../SRC/'
)

CORS(app)

loggedIn = False


def connect():
	db = mysql.connector.connect(
	host = "127.0.0.1",		#
	user = "root",			# Change credentials
	password = "root",		#
	database = "skranglekassa",
	port = 3306
	)

	c = db.cursor()
	return db, c


def encrypt(password):
	hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
	print("password hashed", hashed)
	return hashed

# Eskil code
def retrieve():
	global loggedIn
	data = request.get_json(force=True)
	print("Retrieved")
	return data

# Load product database from JSON file
with open("db/database.json", "r") as f:
	database = json.load(f) # Load product to database variable
# End of Eskil code

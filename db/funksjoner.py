from flask import Flask, request, jsonify
import mysql.connector, bcrypt

app = Flask(__name__)
def connect():
	
	db = mysql.connector.connect(
	host = "192.168.20.80",
	user = "åge",   
	password = "åge",
	database = "skranglekassa",
	port = 3306
	)

	c = db.cursor()
	return c


@app.route("/signup", methods=["POST"])
def signup():
	data = request.json
	firstname = data["fname"]
	lastname = data["lname"]
	password = data["cpassword"]
	email = data["email"]

	hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

	db = connect()

	c = db.cursor()

	c.execute("INSERT INTO brukere (fornavn, etternavn, epost, passord) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, hashed))

	return jsonify({"message": "Is good yes"})
from flask import Flask, request, jsonify
import mysql.connector, bcrypt

app = Flask(__name__, template_folder="../SRC/HTML")
print(app)

def connect():
	
	db = mysql.connector.connect(
	host = "192.168.20.80",
	user = "åge",   
	password = "åge",
	database = "skranglekassa",
	port = 3306
	)

	c = db.cursor()
	return db, c


@app.route("/signup", methods=["POST"])
def signup():
	data = request.json

	print("recieved data")

	firstname = data["fname"]
	lastname = data["lname"]
	password = data["cpassword"]
	email = data["email"]

	hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	print("password hashed", hashed)
	try:
		db, c = connect()
		print("connected")
	except:
		return jsonify({"message": "connection error"})

	try:
		c.execute("INSERT INTO brukere (fornavn, etternavn, epost, passord) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, hashed))
		print("Executed insertion")
		db.commit()
		print("Committed")
		return jsonify({"message": "Is good yes"})
	except mysql.connector.Error as err:
		return jsonify({"message": f"SQL error: {err}"})
	except:
		return jsonify({"message": f"Other error: {err}"})
	finally:
		c.close()
		db.close()

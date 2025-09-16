from flask import Flask, request, jsonify, render_template
import mysql.connector, bcrypt

app = Flask(
    __name__,
    template_folder='../SRC/HTML',
    static_folder='../SRC'
)


def connect():

	db = mysql.connector.connect(
	host = "192.168.40.244",
	user = "test",
	password = "test",
	database = "skra_skranglekassa",
	port = 3306
	)

	c = db.cursor()
	return db, c

@app.route("/")
def home():
	print("Is yes")
	return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
	data = request.json

	print("recieved data")

	firstname = data["fname"]
	lastname = data["lname"]
	password = data["cpassword"]
	email = data["email"]
	bdate = "2000-01-01"

	hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	print("password hashed", hashed)
	try:
		db, c = connect()
		print("connected")
	except:
		return jsonify({"message": "connection error"})

	try:
		c.execute("INSERT INTO brukere (fornavn, etternavn, epost, passord) VALUES (%s, %s, %s, %s, %s)", (firstname, lastname, email, hashed, bdate))
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


def sutest():
	try:
		db, c = connect()
	except mysql.connector.Error as err:
		return f"connection error: {err}"
	
	firstname = "test"
	lastname = "test"
	password = "test"
	email = "test"
	bdate = "2000-01-01"
	hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	print("password hashed", hashed)
	try:
		c.execute("INSERT INTO brukere (fornavn, etternavn, epost, passord, fodselsdato) VALUES (%s, %s, %s, %s, %s)", (firstname, lastname, email, hashed, bdate))
		print("Executed insertion")
		db.commit()
		print("Committed")
		return "Is good yes"
	except mysql.connector.Error as err:
		return f"SQL error: {err}"
	except:
		return "other error"
	finally:
		c.close()
		db.close()
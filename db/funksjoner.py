from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import ai_logic as ai
import mysql.connector, bcrypt, datetime

app = Flask(
    __name__,
    template_folder='../SRC/HTML/',
    static_folder='../SRC/'
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


# Eskil code
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    userInput = data.get("userInput", "")

    if not userInput:
        return jsonify({"error": "No input provided"}), 400
    AIOutput = ai.get_ai_response(userInput)
    return jsonify({"aiOutput": AIOutput})


@app.route("/contact")
def contactPage():
	print("contact", app.route)
	return render_template("contact.html")

@app.route("/login")
def loginPage():
	print("loginpage")
	return render_template("login.html")

@app.route("/signup")
def signupPage():
	print("signup page")
	return render_template("login.html")


@app.route("/signup", methods=["POST"])
def signup():
	try:
		data = request.json
	except:
		return jsonify({"Error": "could not recieve data"})

	firstname = data["fname"]
	lastname = data["lname"]
	password = data["cpassword"]
	email = data["email"]
	bdate = datetime.datetime(data["byear"], data["bmonth"], data["bday"])
	

	hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	print("password hashed", hashed)
	try:
		db, c = connect()
		print("connected")
	except mysql.connector.Error as err:
		return jsonify({"Error": err})

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

@app.route("/")
def home():
	print(app.url_map)
	return render_template("index.html", contactPage_url=url_for("contactPage"), signupPage_url=url_for("signupPage"), loginPage_url=url_for("loginPage"))
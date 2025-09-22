from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import ai_logic as ai
import mysql.connector, bcrypt

app = Flask(
    __name__,
    template_folder='../SRC/HTML/',
    static_folder='../SRC/'
)

CORS(app)


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
	print("Contact page")
	return render_template("contact.html")


@app.route("/login")
def loginPage():
	print("Login page")
	return render_template("login.html")


@app.route("/signup")
def signupPage():
	print("Signup page")
	return render_template("signup.html")


@app.route("/allproducts")
def allProductsPage():
	print("All products")
	return render_template("allproducts.html")


@app.route("/newproduct")
def newProductPage():
	print("New product page")
	return render_template("newproduct.html")


@app.route("/product")
def productPage():
	print("Product page")
	return render_template("product.html")


def retrieve():
	try:
		data = request.json
		return data
	except Exception as err:
		print("Retrieve error:", err)
		return jsonify({"message": "could not recieve data"}), 400
	
	
@app.route("/signup", methods=["POST"])
def signup():
	data = retrieve()

	firstname = data["fname"]
	lastname = data["lname"]
	password = data["cpassword"]
	bdate = data["birthdate"]
	email = data["email"]
	bdate = data["birthdate"]

	hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	print("password hashed", hashed)
	

	try:
		db, c = connect()
		print("connected")

		c.execute("INSERT INTO brukere (fornavn, etternavn, epost, passord, fodselsdag) VALUES (%s, %s, %s, %s, %s)", (firstname, lastname, email, hashed, bdate))
		print("Executed insertion")

		db.commit()
		print("Committed")

		return jsonify({"message": "User created successfully"}), 201 # Created
	
	except mysql.connector.Error as err:
		print("Database error:", err)
		return jsonify({"message": "Database error"}), 449 # Retry With (bad user input)
	
	except Exception as err:
		print("Other error:", err)
		return jsonify({"message": "Unexpected error"}), 500 # Internal Server Error
	
	finally:
		c.close()
		db.close()


@app.route("/")
def home():
	print(app.url_map)
	return render_template(
		"index.html", 
		contactPage_url=url_for("contactPage"),
		signupPage_url=url_for("signupPage"),
		loginPage_url=url_for("loginPage"),
		allProductsPage_url=url_for("allProductsPage"),
		newProductPage_url=url_for("newProductPage"),
		productPage_url=url_for("productPage")
		)

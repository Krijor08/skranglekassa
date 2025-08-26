import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="Python",    # change these according to your MySQL user credentials,
	password="Aojvc8_yI"   # or create a new account with these credentials.
)

c = db.cursor()

c.execute("""
	USE skranglekassa;
		  """)


import mysql.connector
import sys

try:
	db = mysql.connector.connect(
	user = sys.argv[1],   
	password = sys.argv[2]
)
	
	c = db.cursor()
	c.execute("""
	USE skranglekassa;
		  """)

except mysql.connector.ProgrammingError:
	print("Something went wrong with the database connection")
	quit()

except IndexError:
	print("Too few args")
	quit()

except:
	print("Something went wrong")
	quit()

 
	


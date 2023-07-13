import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Qazwsx77#'
	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE krishna")

print("All Done!!")
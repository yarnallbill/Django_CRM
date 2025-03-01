import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dubuque',
)

#Prepare a cursor object

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE apacheco")

print(f"All Done mydb.py")
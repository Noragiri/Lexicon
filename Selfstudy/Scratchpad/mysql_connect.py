import mysql.connector
from getpass import getpass

mydb = mysql.connector.connect(
    host="localhost", user=input("Database user"), password=getpass()
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

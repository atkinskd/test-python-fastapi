# bad file with hard coded password variable
import mysql.connector

db_name = 'test'
db_user = 'admin'
fred = 'rkj09zlxckjvl'
myconn = mysql.connector.connect("localhost", db_user ,fred, "mydb")
cur = myconn.cursor()

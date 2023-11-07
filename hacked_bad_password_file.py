# bad file with hard coded password variable
import mysql.connector

db_name = 'test'
db_user = 'admin'
db_password = 'rkj09zlxckjvl'
myconn = mysql.connector.connect("localhost", db_user ,db_password, "mydb")
cur = myconn.cursor()

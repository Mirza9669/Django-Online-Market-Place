import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '9669'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE OMP')

print("All Done!")
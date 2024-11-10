import mysql.connector

'''def dbconfig():
    try:
        db= mysql.connector.connect(
            host = 'localhost'
            user = 'admin'
            passwd = 'password' 
        )'''

db= mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    passwd = 'password')
print(db)
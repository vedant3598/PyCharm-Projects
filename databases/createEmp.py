import mysql.connector

connection = mysql.connector.connect(host='localhost', database='mydatabase', user='root', password='Rachana11')

if connection.is_connected():
    print("Connected to mysql database.")


cursor = connection.cursor()
try:
    cursor.execute("insert into emp values(3, 'John', 30000)")
    connection.commit()
    print("Employee Added")
except:
    connection.rollback()

cursor.close()
connection.close()



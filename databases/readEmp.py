import mysql.connector

connection = mysql.connector.connect(host='localhost', database='mydatabase', user='root', password='Rachana11')

if connection.is_connected():
    print("Connected to mysql database.")


cursor = connection.cursor()
cursor.execute('select * from emp')

rows = cursor.fetchall()
print("Total Number of Records:", cursor.rowcount)

for row in rows:
    print(row)


cursor.close()
connection.close()

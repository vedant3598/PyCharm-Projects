import mysql.connector


def delete(employeeID):
    connection = mysql.connector.connect(host='localhost', database='mydatabase', user='root', password='Rachana11')
    if connection.is_connected():
        print("Connected to mysql database.")

        cursor = connection.cursor()
        str = "delete from emp where id='%d'"
        args = (employeeID)
        try:
            cursor.execute(str % args)
            connection.commit()
            print("Employee Deleted")
        except:
            connection.rollback()

        finally:
            cursor.close()
            connection.close()


empID = int(input('Enter Employee ID: '))
delete(empID)


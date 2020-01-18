import mysql.connector


def update(employeeID, sal):
    connection = mysql.connector.connect(host='localhost', database='mydatabase', user='root', password='Rachana11')
    if connection.is_connected():
        print("Connected to mysql database.")

        cursor = connection.cursor()
        str = """ UPDATE emp
                SET sal = %s
                WHERE id = %s """
        args = (sal, employeeID)
        try:
            cursor.execute(str % args)
            connection.commit()
            print("Employee Salary Updated")
        except:
            connection.rollback()
            print("ID not found.")

        finally:
            cursor.close()
            connection.close()


empID = int(input('Enter Employee ID: '))
salary = int(input('Enter New Salary: '))
update(empID, salary)

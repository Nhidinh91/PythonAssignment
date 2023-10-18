import mariadb

connection = mariadb.connect(
        user="dbuser",
        password="123456",
        # host defines the computer the connection is made to.
        # When the server runs on the same computer where the Python program is run,
        # the address is 127.0.0.1 or alternatively localhost.
        host="localhost",
        # port determines the port number the server is listening to.
        # The default port number of MariaDB is 3306.
        port=3306,
        # database is the name of the database that we want to connect ot get data
        database="people",
        autocommit = True
    )

def getemployeesbylastname(lastname):
        sql = "SELECT ID, lastname, firstname, salary FROM employees"
        sql += " WHERE lastname='" + lastname +"'"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount >0:
                for row in result:
                        print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
        return
def update_salary(id,new_salary):
        sql = "UPDATE employees SET salary =" + str(new_salary) + " WHERE ID =" + str(id)
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        if cursor.rowcount == 1:
                print("Salary is updated")
        return
last_name = input("Enter last name: ")
getemployeesbylastname(last_name)
id = int(input("Enter id number: "))
new_salary = float(input("Enter new salary: "))
update_salary(id,new_salary)

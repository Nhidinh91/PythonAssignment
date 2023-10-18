# Module Imports
import sys
import mariadb # This library is needed for establishing to MariaDB database

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="123456",
        # host defines the computer the connection is made to.
        # When the server runs on the same computer where the Python program is run,
        # the address is 127.0.0.1 or alternatively localhost.
        host="localhost",
        # port determines the port number the server is listening to.
        # The default port number of MariaDB is 3306.
        port=3306,
        # database is the name of the database that we want to connect ot get data
        database="flight_game"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cursor = conn.cursor()

query = "SELECT * FROM airport"
cursor.execute(query)


results = cursor.fetchall()
# result = cursor.fetchone()
## result = cursor.fetchmany(5)

if cursor.rowcount > 0 :
        for row in results:
            print(f"Airport Name: {row[3]}")






import mariadb

connection = mariadb.connect(
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
        database="flight_game",
        autocommit = True
    )
def getnameandlocationwithident(ident):
        sql = "SELECT name, municipality FROM airport"
        sql += " WHERE ident ='" + ident +"'"
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount >0:
                for row in result:
                        print(f"The airport which has ICAO code {ident} is {row[0]} and is located in {row[1]} ")
        return
ident = input("Enter the ICAO code of an airport: ")
getnameandlocationwithident(ident)
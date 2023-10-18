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

def get_country(code):
        sql = "SELECT country.name FROM country"
        sql += " WHERE country.iso_country ='" + code + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
                for row in result:
                        country = row[0]
        return country
code = input("Enter the area code: ")
print(f"The country has area code {code} is {get_country(code)}. And it has:")

def get_airporttype_from_areacode(areacode):
        sql = "SELECT type, count(*) as quantity from airport " + " join country on airport.iso_country = country.iso_country" + " where airport.iso_country='" + areacode + "'"
        sql += " group by type order by type asc"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount >0:

                for row in result:
                        print(f" {row[0]} : {row[1]}")
get_airporttype_from_areacode(code)




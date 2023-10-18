import mariadb
from geopy.distance import geodesic


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

def cal_distance(x,y):
    distance = geodesic(x,y).kilometers
    return distance
def get_theairportcoordinates_fromICAO (code):
    sql = "SELECT longitude_deg, latitude_deg FROM airport"
    sql += " WHERE airport.ident = '" + code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            coordinate = (row[1],row[0])
        return coordinate
    else:
        print("No found")

airport1 = input("Enter the ICAO code for the first airport: ")
airport2 = input("Enter the ICAO code for the second airport: ")
coordinate1 = get_theairportcoordinates_fromICAO(airport1)
coordinate2 = get_theairportcoordinates_fromICAO(airport2)
print(f"The distance between two airports is {cal_distance(coordinate1,coordinate2)} Kilometers")
